import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    def __init__(self, v0, kut, x0=0, y0=0, Cd=0.47, metoda="Euler"):
        self.metoda = metoda
        self.v0 = v0
        self.kut = np.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(self.kut)
        self.vy = v0 * np.sin(self.kut)
        self.Cd = Cd
        self.g = 9.81
        self.r = 0.05
        self.rho = 1.28
        self.m = 0.5

        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.t = 0
        self.x_lista = [self.x]
        self.y_lista = [self.y]

    def move_euler(self, dt):
        v = np.sqrt(self.vx**2 + self.vy**2)
        A = np.pi * self.r**2
        c = 0.5 * self.Cd * self.rho * A

        ax = -(c/self.m) * v * self.vx
        ay = -self.g - (c/self.m) * v * self.vy

        self.vx += ax * dt
        self.vy += ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.t += dt

        self.x_lista.append(self.x)
        self.y_lista.append(self.y)

    def move_rk4(self, dt):
        A = np.pi * self.r**2
        c = 0.5 * self.Cd * self.rho * A

        # k1
        v = np.sqrt(self.vx**2 + self.vy**2)
        ax = -(c/self.m) * v * self.vx
        ay = -self.g - (c/self.m) * v * self.vy

        k1_vx = ax
        k1_vy = ay
        k1_x = self.vx
        k1_y = self.vy

        # k2
        vx = self.vx + 0.5 * dt * k1_vx
        vy = self.vy + 0.5 * dt * k1_vy
        v_temp = np.sqrt(vx**2 + vy**2)

        ax = -(c/self.m) * v_temp * vx
        ay = -self.g - (c/self.m) * v_temp * vy

        k2_vx = ax
        k2_vy = ay
        k2_x = vx
        k2_y = vy

        # k3
        vx = self.vx + 0.5 * dt * k2_vx
        vy = self.vy + 0.5 * dt * k2_vy
        v_temp = np.sqrt(vx**2 + vy**2)

        ax = -(c/self.m) * v_temp * vx
        ay = -self.g - (c/self.m) * v_temp * vy

        k3_vx = ax
        k3_vy = ay
        k3_x = vx
        k3_y = vy

        # k4
        vx = self.vx + dt * k3_vx
        vy = self.vy + dt * k3_vy
        v_temp = np.sqrt(vx**2 + vy**2)

        ax = -(c/self.m) * v_temp * vx
        ay = -self.g - (c/self.m) * v_temp * vy

        k4_vx = ax
        k4_vy = ay
        k4_x = vx
        k4_y = vy

        self.vx += (dt/6) * (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx)
        self.vy += (dt/6) * (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy)

        self.x += (dt/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        self.y += (dt/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)

        self.t += dt

        self.x_lista.append(self.x)
        self.y_lista.append(self.y)

    def simulacija_usporedba(self, dt=0.01):

        self.reset()
        while self.y >= 0:
            self.move_euler(dt)

        x_euler = self.x_lista.copy()
        y_euler = self.y_lista.copy()

        self.reset()
        while self.y >= 0:
            self.move_rk4(dt)

        x_rk4 = self.x_lista.copy()
        y_rk4 = self.y_lista.copy()

        plt.plot(x_euler, y_euler, label="Euler")
        plt.plot(x_rk4, y_rk4, label="RK4", linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Euler vs RK4 (dt={dt})")
        plt.grid(True)
        plt.legend()
        plt.show()


p = Projectile(v0=50, kut=45)
p.simulacija_usporedba(dt=0.05)

#Ovaj zadatak je riješen uz pomoć umjetne inteligencije.
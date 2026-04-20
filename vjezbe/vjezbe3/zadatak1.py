import matplotlib.pyplot as plt
import numpy as np

class Projectile:
    def __init__(self, v0, kut, x0=0, y0=0,r = 0.05,Cd=0.47): #Cd - koeficijent otpora zraka
      self.v0 = v0
      self.kut = np.radians(kut)
      self.x0 = x0
      self.y0 = y0
      self.x = x0
      self.y = y0
      self.vx = v0 * np.cos(self.kut)
      self.vy = v0 * np.sin(self.kut)
      self.k = Cd
      self.g = 9.81
      self.t = 0
      self.r = r
      self.rho = 1.225
      self.m = 0.5
      self.x_lista = [x0]
      self.y_lista = [y0]

    def reset(self):         
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.t = 0
        self.x_lista = [self.x]
        self.y_lista = [self.y]

    def __move(self, dt=0.001):  
        v = np.sqrt(self.vx**2 + self.vy**2)    
        A = np.pi * self.r**2
        c = 0.5 * self.k * self.rho * A      
        ax = -(c/self.m) * v * self.vx
        ay = -self.g - (c/self.m) * v * self.vy   
        
        self.t += dt
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)

    def simulacija(self):
        dt_values = [0.1, 0.01, 0.001]

        for dt in dt_values:
          self.reset()
          while self.y >= 0:
            self.__move(dt)
          plt.plot(self.x_lista, self.y_lista, label=f"dt={dt}")
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja čestice")
        plt.show()     
  
p = Projectile(v0=50, kut=45)
p.simulacija()
  


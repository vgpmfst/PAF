import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, v0, kut, x0=0, y0=0):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(self.kut)
        self.vy = v0 * np.sin(self.kut)
        self.g = 9.81
        self.t = 0

        self.x_lista = [x0]
        self.y_lista = [y0]

    def reset(self):         #Briše sve podatke o čestici kako bi se druge metode mogle ponovno pozvati.
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.t = 0
        self.x_lista = [self.x]
        self.y_lista = [self.y]

    def __move(self, dt=0.001):            #Pomiče česticu za korak dt.
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.t += dt
        self.vy -= self.g * dt
        self.x_lista.append(self.x)
        self.y_lista.append(self.y)

    def range(self, dt=0.001):        #Računa domet čestice
        self.reset()                #Briše podatke kako bi se simulacija mogla odviti.
        while self.y >= 0:          #numerički pristup; račun se zbiva dok je čestica u zraku
            self.__move(dt)         #poziv privatne metode
        return self.x_lista[-1]     #return vraća rezultat računa u obliku dometa tj. udaljenosti koje je čestica postigla u x smjeru tako da vrati zadnju vrijednost x iz računa.

    def plot_trajectory(self):      #Crtanje putanje u x - y ravnini.
        self.reset()
        while self.y >= 0:
            self.__move(0.01)

        plt.plot(self.x_lista, self.y_lista)
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja čestice")
        plt.show()
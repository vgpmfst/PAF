from particle import Particle
import matplotlib.pyplot as plt
import numpy as np

#analitičko rješenje
v0 = 10
kut = 60
x0 = 0
y0 = 0
g = 9.81
kut_rad = np.radians(kut)
analiticki = (v0**2 * np.sin(2*kut_rad)) /g

rel_error = []
dt_lista = []

for dt in np.linspace(0.01, 1, 100):
#numeričko rješenje
    p1 = Particle(v0,kut,x0,y0)
    numericki = p1.range(dt)
    error = (abs(analiticki-numericki)/analiticki)*100
    rel_error.append(error)
    dt_lista.append(dt)

plt.xlabel("dt[s]")
plt.ylabel("absolute relative error[%]")
plt.title("Absolute relative error for range of projectile")
plt.grid(True)
plt.plot(dt_lista, rel_error)
plt.show(block=True)



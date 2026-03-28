from particle import Particle
import numpy as np

#analitičko rješenje
v0 = 10
kut = 45
x0 = 0
y0 = 0
g = 9.81
kut_rad = np.radians(kut)
analiticki = (v0**2 * np.sin(2*kut_rad)) /g

#numeričko rješenje
p1 = Particle(v0,kut,x0,y0)
numericki = p1.range(dt=0.001)
p1.plot_trajectory()

print("Analitički domet:", analiticki)
print("Numerički domet:",numericki )

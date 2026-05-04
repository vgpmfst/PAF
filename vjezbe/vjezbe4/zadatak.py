import numpy as np
import matplotlib.pyplot as plt

q=1.602e-19 #c
m=9.11e-31 #kg
B = np.array([0.0,0.0,1.0])
E = np.array([0.0,0.0,0.0])
v0 = np.array([1.0,1.0,1.0])
r0 = np.array([0.0,0.0,0.0])
dt = 1e-14 #s

def simulacija_gibanja(q):
   r = np.zeros((10000, 3))
   v = np.zeros((10000, 3))
    
   r[0] = r0
   v[0] = v0
   
   for i in range(10000):
        a = (q / m) * (E + np.cross(v[i], B))
        v[i+1] = v[i] + a * dt
        r[i+1] = r[i] + v[i+1] * dt
   return r

r_elektron = simulacija_gibanja(q=-1.602e-19)
r_pozitron = simulacija_gibanja(q=1.602e-19)


ax = plt.axes(projection='3d')
ax.plot(r_elektron[:,0], r_elektron[:,1], r_elektron[:,2],label='elektron')
ax.plot(r_pozitron[:,0], r_pozitron[:,1], r_pozitron[:,2], label='proton')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
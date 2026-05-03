#Newton - Lorentzova jednadžba: F = ma = q(E + v*B)
#Položaj: r = (x,y,z), Brzina v: v= (vx,vy,vz), Akceleracija: a = (dvx/dt,dvy/dt,dvz/dt)
#za B = (0,0,B) i E = (Ex,Ey,Ez), vektroski produkt v x B = (vyB,-vxB,0)
#sustav diferencijalnih jednadžbi: dvx/dt = (q/m)(Ex + vyB), dvy/dt = (q/m)(Ey - vxB), dvz/dt = (q/m)Ez
#Kada je E = 0, v0 = (vx0,vy0,vz0)-->
# -> Gibanje u z smjeru: z(t) = z0 + vz0*t
# -> Gibanje u xy ravnini: Kombinacijom prve dvije jednadžbe dobivamo opis kružnog gibanja s kutnom frekvencijom
# ω = qB/m
#Rješenje za x i y komponente su harmonijske funkcije. Rezultat je uniformno kružno gibanje u $xy$-ravnini.
#Kombinacijom jednolikog gibanja po pravcu (z-os) i kružnog gibanja (xy-ravnina), čestica iscrtava helikoidnu putanju (spiralu)
#Elektron i pozitron će imati istu putanju samo u različitom smjeru.
import numpy as np
import matplotlib.pyplot as plt

q=1.602e-19 #c
m=9.11e-31 #kg
B = np.array([0,0,1])
E = np.array([0,0,0])
v0 = np.array([1,1,1])
r0 = np.array([0,0,0])
dt = 1e-14 #s
def simulacija_gibanja(q):
   r = np.zeros((4000, 3))
   v = np.zeros((4000, 3))
    
   r[0] = r0
   v[0] = v0
   
   for i in range(3999):
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
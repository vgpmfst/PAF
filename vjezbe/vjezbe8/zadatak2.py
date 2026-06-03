import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

kut_deg = np.array([0 , 5 , 10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50 , 55 , 60 , 65 , 70 , 75 , 80 , 85])

T_120 = np.array([0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 ,0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 ,2.5460])
T_240 = np.array([1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 ,1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 ,3.1573])

L1 = 0.120 #m
L2 = 0.240 #m

g = 9.81
theta = np.radians(kut_deg)

def period(theta,l):
    return 2*np.pi*np.sqrt(l/(g*np.cos(theta)))

#curve_fit
param120, covs120 = curve_fit(period,theta,T_120) #program pokušava pronaći vrijednost parametra l da teorijska krivulja bude što bliže mjerenjima
param240, covs240 = curve_fit(period,theta,T_240)

fit120 = param120[0] #cruve_fit stvara array koji sadrži parametar koji je najbliži modelu i podatcima koje smo unijeli
fit240 = param240[0]

theta_fit = np.linspace(0, np.radians(85), 100) #stvaramo novi array kutova da krivulja bude glatka

plt.scatter(kut_deg, T_120,label = "L = 120mm")
plt.scatter(kut_deg, T_240,label= "L = 240mm")
plt.plot(np.degrees(theta_fit), period(theta_fit, fit120), label=f"Fit L=120 mm (l={fit120} m)")
plt.plot(np.degrees(theta_fit), period(theta_fit, fit240), label=f"Fit L=240 mm (l={fit240} m)")
plt.xlabel("Kut theta [stupnjevi]")
plt.ylabel("Period T [sekunde]")
plt.title("Fizikalno njihalo")
plt.legend()
plt.show()

rel_pogreska120 = (abs(fit120-0.120)/0.120)*100
rel_pogreska240 = (abs(fit240-0.240)/0.240)*100

print(f"Relativna pogreška za L=120mm:{rel_pogreska120}")
print(f"Relativna pogreška za L=240mm:{rel_pogreska240}")

#Ispravnost koda je provjerio AI


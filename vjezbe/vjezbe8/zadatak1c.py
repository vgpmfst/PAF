import numpy as np
import matplotlib.pyplot as plt
import math

h0 = 0.54 # m
m = 0.5257 # kg
r = 4.025e-3 # m
g = 9.81 #m/s^2
h = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40] # m
t_mean = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813] # s

h = np.array(h)
t_mean = np.array(t_mean)

#a)
s = h0 - h

n = len(h)

x = t_mean**2
y = s

a = (n*np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2) #nagib
b = (np.sum(y) - a*np.sum(x)) / n #odsječak

fit = a * t_mean + b  

# Reziduali; razlika između izmjerenih vrijednosti i modela kojega smo izračunali
residuals = y - fit #Dio za izračun pogrešaka je napravio AI

# Standardna devijacija reziduala; predstavlja procjenu tipične udaljenosti točaka od regresijskog pravca(koristi se n -2 zato što procjenjujemo dva parametra pa gubimo dva stupnja slobode)
sigma_y = np.sqrt(np.sum(residuals**2) / (n - 2))

# Pogreška nagiba
sigma_a = sigma_y*np.sqrt( n/(n*np.sum(x**2)-np.sum(x)**2))


# Pogreška odsječka
sigma_b = sigma_y*np.sqrt(
    np.sum(x**2)/(n*np.sum(x**2)-np.sum(x)**2)
)

print(f"Nagib a = {a:.4f} ± {sigma_a:.4f}")


#zadatak 1(c):

#moment tromosti
akc = 2*a # s = 0.5akc*t^2 --> akc = 2*a(nagib)
I = (m*r**2)*((g/akc) - 1)

#propagacija pogreške I_z:
# sigma_I = |deriv_I po a|*sigma_a
sigma_I = ((m*(r**2)*g)/(2*(a**2)))*sigma_a

print(f"Moment tromosti: {I:.3e},pripadna izvedena pogreška: {sigma_I:.3e}")

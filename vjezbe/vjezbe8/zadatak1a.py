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

log_s = np.log(s)
log_t = np.log(t_mean)

n = len(h)

a = (n * np.sum(log_t * log_s) - np.sum(log_t) * np.sum(log_s)) / (n * np.sum(log_t**2) - np.sum(log_t)**2) # nagib
b = (np.sum(log_s) - a * np.sum(log_t)) / len(log_t) #odsječak

print(f"Nagib na pravac je{a:.2f}")
print(f"Osječak na pravac je{b:.2f}")

fit = a * log_t + b  # Ovaj dio je ispravio AI

plt.scatter(log_t, log_s)
plt.plot(log_t,fit,label="fit")
plt.xlabel('log(t)')
plt.ylabel('log(s)')
plt.show()


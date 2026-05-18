import math
import numpy as np
import matplotlib.pyplot as plt
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336]) #Nm
φ = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) #rad

#y = ax + b; M = Dt*φ --> a = Dt
a = np.sum(φ*M)/np.sum(φ**2)
s_a = np.sqrt((1/len(M)) * (np.sum(M**2) / np.sum(φ**2) - a**2))

x_fit = np.linspace(0, 1.1, 100)
y_fit = a * x_fit
print("Dt =",a)
print("sigma Dt =", s_a)

plt.xlabel("φ/rad")
plt.ylabel("M/Nm")
plt.grid()
plt.scatter(φ, M, label="parametri")
plt.plot(x_fit,y_fit,label="Linearna regresija",)
plt.legend()
plt.show()

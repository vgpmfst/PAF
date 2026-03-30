import matplotlib.pyplot as plt
import numpy as np
import calculus

#Kubna funkcija
def f(x):
    return x**3 - 2*x**2 + x
def f_der(x):
    return 2*x**2 - 4*x + 1 #analitička derivacija

#Ova linija vraća vrijednosti točaka x i njihovih derivacija iz metode derivacija_raspon.
x, d1 = calculus.derivacija_raspon(f, -5, 5, ϵ=1e-5)
x, d2 = calculus.derivacija_raspon(f, -5, 5, ϵ=1e-3)
x, d3 = calculus.derivacija_raspon(f, -5, 5, ϵ=1e-1)

#Plotanje grafa
plt.plot(x, f_der(x), label="Analitička")
plt.plot(x, d1, c = "g", label="ε=1e-5")
plt.plot(x, d2, c = "b", label="ε=1e-3")
plt.plot(x, d3, c = "r", label="ε=1e-1")
plt.title("Kubna funkcija")
plt.legend()
plt.grid()
plt.figure()  #Stvara figuru na kojoj se mogu prikazivati oba grafa.

#Trigonometrijska funkcija
def g(x):
    return np.sin(x)

def g_der(x):
    return np.cos(x)
#Ova linija vraća vrijednosti točaka x i njihovih derivacija iz metode derivacija_raspon.
x, d = calculus.derivacija_raspon(g, 0, 2*np.pi, ϵ=1e-5)

plt.plot(x, g_der(x), label="Analitička")
plt.plot(x, d, c = "r", label="ε=1e-5")
plt.title("Sinus funkcija")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

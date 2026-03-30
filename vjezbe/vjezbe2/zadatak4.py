import numpy as np
import matplotlib.pyplot as plt
import calculus

def f(x):
    return x**2

# analitički integral
def F(x):
    return x**3 / 3

a,b = 0, 3

koraci = [10, 50, 100, 500]

analiticki = F(b) - F(a)

prav_donja = []
prav_gornja = []
trapez = []

for n in koraci:
    d, g = calculus.integral_pravokutnici(f, a, b, n)
    t = calculus.integral_trapez(f, a, b, n)

    prav_donja.append(d)
    prav_gornja.append(g)
    trapez.append(t)

# crtanje grafa
plt.plot(koraci, [analiticki]*len(koraci), label="Analitičko")
plt.plot(koraci, prav_donja, c = "r", label="Pravokutnici (donja)")
plt.plot(koraci, prav_gornja, c = "g", label="Pravokutnici (gornja)")
plt.plot(koraci, trapez, c = "b", label="Trapez")
plt.xlabel("Broj podjela")
plt.ylabel("Vrijednost integrala")
plt.title("Numerička integracija")
plt.legend()
plt.grid()
plt.show()
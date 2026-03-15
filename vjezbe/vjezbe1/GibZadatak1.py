import matplotlib.pyplot as plt
import numpy as np

m = float(input("Unesite masu čestice u kg: "))
F = float(input("Unesite silu koja djeluje na česticu: "))

a = F/m
t = np.linspace(0, 10, 100)

v = a*t
x = 0.5*a*t**2

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title("x - t graf")
plt.xlabel("t (s)")
plt.ylabel("x (m)")

plt.subplot(3,1,2)
plt.plot(t, v)
plt.title("v - t graf")
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")

plt.subplot(3,1,3)
plt.plot(t, [a]*len(t)) #Ai je pomogao kod ove linije jer je kod pucao te je uveo t kao np.linspace.
plt.title("a - t graf")
plt.xlabel("t (s)")
plt.ylabel("a (m/s²)")

plt.tight_layout()
plt.show()
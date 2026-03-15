import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, t_max=10, broj_tocka=100):

    a = F / m
    t = np.linspace(0, t_max, broj_tocka)

    v = a * t
    x = 0.5 * a * t**2

    plt.figure(figsize=(10,8))

    plt.subplot(3,1,1)
    plt.plot(t, x, 'b')
    plt.title("x - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.grid(True)

    plt.subplot(3,1,2)
    plt.plot(t, v, 'g')
    plt.title("v - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.grid(True)

    plt.subplot(3,1,3)
    plt.axhline(y=a, color='r')
    plt.title("a - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("a (m/s²)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
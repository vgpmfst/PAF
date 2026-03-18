import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):

    a = F / m
    t = np.linspace(0, 10, 100)

    v = a * t
    x = 0.5 * a * t**2


    plt.subplot(3,1,1)
    plt.plot(t, x, color='blue')
    plt.title("x - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.grid(True)

    plt.subplot(3,1,2)
    plt.plot(t, v, color='green')
    plt.title("v - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.grid(True)

    plt.subplot(3,1,3)
    plt.plot(t, [a]*len(t), color='red')
    plt.title("a - t graf")
    plt.xlabel("t (s)")
    plt.ylabel("a (m/s²)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
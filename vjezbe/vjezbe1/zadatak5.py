import matplotlib.pyplot as plt

def funkcija():
    x1 = int(input("Unesite x koordinatu 1. točke: "))
    y1 = int(input("Unesite y koordinatu 1. točke: "))
    x2 = int(input("Unesite x koordinatu 2. točke: "))
    y2 = int(input("Unesite y koordinatu 2. točke: "))
    if x2 == x1:
        print("x1 i x2 ne smiju biti jednaki!")
        return
    m = (y2 - y1) / (x2 - x1)
    c = y2 - m * x2
    x = [x1, x2]
    y = [y1, y2]
    print(f"y = {m}x + {c}")
    broj = int(input("Za prikaz grafa unesite 1, za spremanje u PDF unesite 2: "))
    ime = input("Unesite ime grafa: ")
    if broj not in [1,2]:
        print("Unesite ispravan broj!")
        return
    plt.plot(x, y, marker='o')
    plt.title(ime)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    if broj == 2:
        plt.savefig("zadatak5.pdf", format="pdf", bbox_inches="tight")
    plt.show()

funkcija()
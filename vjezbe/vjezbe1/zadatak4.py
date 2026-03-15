def funkcija():
    x1 = int(input("Unesite x koordinatu 1.točke: "))
    y1 = int(input("Unesite y koordinatu 1.tocke: "))
    x2 = int(input("Unesite x koordinatu 2.točke: "))
    y2 = int(input("Unesite y koordinatu 2.točke: "))
    if x2 == x1:
        print("x1 i x2 ne smiju biti jednaki!")
    m = (y2 - y1)/(x2 - x1)
    c = y2 - m*x2
    print (f"y = {m}x + {c}")
funkcija()
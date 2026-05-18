def funkcija():
    N = int(input("Unesite broj iteracija: "))
    x= 0
    y= 5
    for i in range(1,N+1):
        x += (1/3)
        y -= (1/3)
    print(x,y)
funkcija()
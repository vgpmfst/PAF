import matplotlib.pyplot as plt
import numpy as np

def deriviranje_tocka(f,x,ϵ=0.00001,metoda="three-step"):
    if metoda == "three-step":
        return (f(x + ϵ) - f(x - ϵ)) / (2 * ϵ)
    elif metoda == "two-step":
         return (f(x+ϵ)-f(x))/ϵ
    else:
        print("Neispravna metoda!")

def derivacija_raspon(f,donja,gornja,ϵ=0.00001,metoda="three-step"):
    if donja > gornja:
        print("Donja granica funkcije mora biti manja ili jednaka gornjoj!")    
        return

    korak = (gornja - donja)/100
    x = np.linspace(donja,gornja,100)

    if metoda == "three-step":
            derivacija = (f(x + ϵ) - f(x - ϵ)) / (2 * ϵ)
    elif metoda == "two-step":
            derivacija =(f(x+ϵ)-f(x))/ϵ
    else:
            print("Neispravna metoda!")
            
    return x, derivacija

#Integracija uz pomoć pravokutne aproksimacije
def integral_pravokutnici(f,donja,gornja,n):
    if donja > gornja:
        print("Donja granica funkcije mora biti manja ili jednaka gornjoj!")    
        return
    x = np.linspace(donja, gornja, n)

    dx = (gornja - donja) / n

    donja_suma = 0
    gornja_suma = 0

    for i in range(n):
        lijeva = f(x[i])
        desna = f(x[i])

        donja_suma += min(lijeva, desna) * dx
        gornja_suma += max(lijeva, desna) * dx

    return donja_suma, gornja_suma

#Integriranje uz pomoć trapezne formule
def integral_trapez(f, donja, gornja, n):
    if donja > gornja:
        print("Donja granica mora biti manja ili jednaka gornjoj!")
        return

    x = np.linspace(donja, gornja, n)

    dx = (gornja - donja) / n

    suma = 0

    for i in range(1, n):
        suma += f(x[i])

    integral = dx * ( (f(x[0]) + f(x[-1]))/2 + suma )

    return integral

#Za ovaj zadatak je pomogao Ai.
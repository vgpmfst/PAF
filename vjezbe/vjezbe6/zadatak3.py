import arithm
import math
import numpy as np

Valjak1 = [138.92, 138.98, 139.20, 138.90, 138.92]#g
Valjak2 = [128.65, 128.60, 128.65, 128.35, 128.50]#g
Valjak3 = [71.89, 71.90, 71.79, 71.85, 71.70]#g

m1=arithm.aritm_sredina(5,Valjak1)
m2=arithm.aritm_sredina(5,Valjak2)
m3=arithm.aritm_sredina(5,Valjak3)

valjak1 = [19.98/20 ,20.18/20, 20.10/20, 20.08/20, 19.74/20]#mm
valjak2 = [19.92/20, 19.82/20, 19.96/20, 19.98/20, 19.88/20]#mm
valjak3 = [24.96/20, 24.98/20, 24.98/20, 24.92/20, 24.94/20]#mm

R1=arithm.aritm_sredina(5,valjak1)
R2=arithm.aritm_sredina(5,valjak2)
R3=arithm.aritm_sredina(5,valjak3)

valjak11 = [49.80/10, 49.00/10, 50.48/10, 49.80/10, 49.96/10] #mm
valjak22 =  [52.56/10, 52.50/10, 52.62/10, 52.58/10, 52.54/10]#mm
valjak33= [55.34/10, 55.40/10, 55.30/10, 55.44/10, 55.48/10]#mm

L1=arithm.aritm_sredina(5,valjak11)
L2=arithm.aritm_sredina(5,valjak22)
L3=arithm.aritm_sredina(5,valjak33)



def volumen_valjka(R,L):
    V = (R**2)*math.pi*L
    print("volumen valjka:",f"{V:e}","cm^3")
    return(V)


def gustoća_valjka(V,m):
    ρ=m/V
    print("Gustoća valjka:",ρ,"g/cm^3")
    return(ρ)

V1=volumen_valjka(R1,L1)
V2=volumen_valjka(R2,L2)
V3=volumen_valjka(R3,L3)

ρ1=gustoća_valjka(V1,m1)
ρ2=gustoća_valjka(V2,m2)
ρ3=gustoća_valjka(V3,m3)


import math
import numpy as np
import arithm

valjak1 = [19.98/20 ,20.18/20, 20.10/20, 20.08/20, 19.74/20]#mm
valjak2 = [19.92/20, 19.82/20, 19.96/20, 19.98/20, 19.88/20]#mm
valjak3 = [24.96/20, 24.98/20, 24.98/20, 24.92/20, 24.94/20]#mm

R1=arithm.aritm_sredina(5,valjak1)
sigma_R1=arithm.standardna_devijacija(5,valjak1)
R2=arithm.aritm_sredina(5,valjak2)
sigma_R2=arithm.standardna_devijacija(5,valjak2)
R3=arithm.aritm_sredina(5,valjak3)
sigma_R3=arithm.standardna_devijacija(5,valjak3)

valjak11 = [49.80/10, 49.00/10, 50.48/10, 49.80/10, 49.96/10] #mm
valjak22 =  [52.56/10, 52.50/10, 52.62/10, 52.58/10, 52.54/10]#mm
valjak33= [55.34/10, 55.40/10, 55.30/10, 55.44/10, 55.48/10]#mm

L1=arithm.aritm_sredina(5,valjak11)
sigma_L1=arithm.standardna_devijacija(5,valjak11)
L2=arithm.aritm_sredina(5,valjak22)
sigma_L2=arithm.standardna_devijacija(5,valjak22)
L3=arithm.aritm_sredina(5,valjak33)
sigma_L3=arithm.standardna_devijacija(5,valjak33)


def volumen_valjka(R,L):
    V = (R**2)*math.pi*L
    print("volumen valjka:",f"{V:e}","cm^3")

def sigma_volumena(R, sigma_R, L, sigma_L):
      V = math.pi * R**2 * L
      sigma = V * math.sqrt((2 * sigma_R / R)**2 +(sigma_L / L)**2)
      print("Standardna devijacija volumena:",f"{sigma:.3e} cm^3")

volumen_valjka(R1,L1),sigma_volumena(R1, sigma_R1, L1, sigma_L1)
volumen_valjka(R2,L2),sigma_volumena(R2, sigma_R2, L2, sigma_L2)
volumen_valjka(R3,L3),sigma_volumena(R3, sigma_R3, L3, sigma_L3)
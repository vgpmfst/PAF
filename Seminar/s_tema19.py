import numpy as np
import matplotlib.pyplot as plt

#parametri
g = 9.81 #m/s^2
m = 80 #kg
p0 = 101325 #Pa
T0 = 288.16 #K
k =  1.3806e-23 #J/k (boltzmannova konstanta)
R = 8.3144 #J/mol*K (Univerzalna plinska konstanta)
alpha = 0.0065 #Temperaturni gradijent od 0 do 11000m, koristi se u barometarskoj formuli
M = 0.0289644      # kg/mol, masa suhog zraka

#prije otvora padobrana
C1 = 1
A1 = 0.70 #m^2
#nakon otpora padobrana
C2 = 1.5
A2 = 22.0  #m^2

#Sigurna brzina: oko 5 do 7 m/s
sigurna_brzina = 7 #m/s

#Uobičajena G-sila koju osjete skakači ide u rasponu od 5 do 7G no veće sile su podnošljive a gornja granica je oko 15G.
G_granica = 7

#Računanje potrebnih podataka
def temperatura(y):
    T = T0 - alpha*y
    return T

def pritisak(y):
    eksponent = (g * M) / (R * alpha)
    return p0 * (1 - (alpha * y) / T0) ** eksponent

def gustoca_zraka(y):
    T = temperatura(y)
    P = pritisak(y)
    return ((P*M)/(R*T))


def simulacija(y0, y_otv, t_otv=3.0, dt=0.01):
    y = y0
    v = 0
    t = 0
    opening = False
    max_G = 0

    vremena = []
    visine = []

    while y > 0:
        rho = gustoca_zraka(y)
        # otvaranje padobrana
        if opening == False and (y <= y_otv):
            opening = True
            t_poc = t
        if opening == False:
            CA = C1*A1
        else:
            faktor = min((t - t_poc)/t_otv, 1.0)
            CA = C1*A1 + faktor*(C2*A2 - C1*A1)

        F = 0.5 * rho * v**2 * CA
        a = g - F/m

        G = abs(a)/g
        max_G = max(max_G, G)

        v += a*dt
        y -= v*dt
        t += dt

        vremena.append(t)
        visine.append(y)

    return v, max_G, vremena, visine

def najniza_sigurna_visina(y0, korak=10):
    for y_otv in range(0, int(y0), korak):
        v_tlo, max_G, vrijeme, visina = simulacija(y0, y_otv)
        if max_G <= G_granica and abs(v_tlo) <= sigurna_brzina:
            return y_otv

    return None  

for y_otv in [1000, 2000, 3000, 4000, 5000]:
    v, G, vrijeme, visina = simulacija(6000, y_otv)
    print(f"y_otv={y_otv} , v={v} , G={G}")


for y0 in range(1000,5000,500):
    y_otv = najniza_sigurna_visina(y0)
    print(f"Minimalna visina otvaranja padobrana na {y0}m je {y_otv} metara.")

#Ovisnost minimalne visine otvora padobrana o visini skoka
y_otvaranja = []
y_skoka = []

for i in range(1000,8000,300):
     y_min = najniza_sigurna_visina(i)
     y_skoka.append(i)
     y_otvaranja.append(y_min)


plt.plot(y_skoka, y_otvaranja)
plt.xlabel("Visina skoka (m)")
plt.ylabel("Minimalna visina otvaranja (m)")
plt.title('Ovisnost minimalne visine otvaranja o visini skoka')
plt.grid(True)
plt.tight_layout() 
plt.show()

v, G, vremena, visine = simulacija(6000, 2000)

plt.plot(vremena, visine)
plt.xlabel("Vrijeme (s)")
plt.ylabel("Visina (m)")
plt.title("Ovisnost visine o vremenu")
plt.grid(True)
plt.tight_layout()
plt.show()
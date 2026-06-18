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
    eksponent = (g*M) / (R*alpha)
    return p0*(1-(alpha*y)/T0) ** eksponent

def gustoca_zraka(y):
    T = temperatura(y)
    P = pritisak(y)
    return ((P*M)/(R*T))

def simulacija(y0, y_otv,C_2, A_2, t_otv=3.0, dt=0.1):
    y = y0
    v = 0
    t = 0

    opening = False
    max_G = 0

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
            CA = C1*A1 + faktor*(C_2*A_2 - C1*A1)

        F = 0.5 * rho * v**2 * CA
        a = g - F/m

        G = abs(a)/g
        max_G = max(max_G, G)

        v += a*dt
        y -= v*dt
        t += dt

    return v, max_G

def sigurno(y0, y_otv):
    v_tlo, max_G = simulacija(y0, y_otv)
    return (max_G <= G_granica) and (abs(v_tlo) <= sigurna_brzina)

def najniza_sigurna_visina(y0, korak=10):
    for y_otv in range(0, int(y0), korak):
        v_tlo, max_G = simulacija(y0, y_otv)
        if max_G <= G_granica and abs(v_tlo) <= sigurna_brzina:
            return y_otv

    return None  

def terminalna_brzina(C, A, rho=1.225):
    return np.sqrt((2*m*g)/(rho*C*A))

def najniza_sigurna_visina(y0, C2, A2):
    for y_otv in range(0, int(y0), 10):
        v_tlo, max_G = simulacija(y0,y_otv,C2,A2)
        if (abs(v_tlo) <= sigurna_brzina and max_G <= G_granica):
            return y_otv

    return None

A_lista = np.linspace(10,40,20)


for A in A_lista:
    y_min = najniza_sigurna_visina(6000,C2,A)
    print(f"A={A}, y_min={y_min}")

visine = []

for A in A_lista:
    y_min = najniza_sigurna_visina(6000,C2,A)
    visine.append(y_min)

plt.plot(A_lista, visine)
plt.xlabel("Površina padobrana A2 (m^2)")
plt.ylabel("Minimalna sigurna visina otvaranja (m)")
plt.title("Utjecaj površine padobrana")
plt.grid()
plt.show()

vt_lista = []
visine_vt = []

for A in A_lista:
    y_min = najniza_sigurna_visina(6000, C2, A)
    if y_min is not None:
        vt = terminalna_brzina(C2, A)
        vt_lista.append(vt)
        visine_vt.append(y_min)


plt.plot(vt_lista, visine_vt)
plt.xlabel("Terminalna brzina nakon otvaranja (m/s)")
plt.ylabel("Minimalna sigurna visina otvaranja (m)")
plt.title("Minimalna visina otvaranja i terminalna brzina")
plt.grid()
plt.show()

vt_lista = []
visine = []
CA_lista = np.linspace(5,60,20)
visine = []

for CA in CA_lista:
    A = CA/C2
    y_min = najniza_sigurna_visina(6000,C2, A)
    visine.append(y_min)


plt.plot(CA_lista, visine)
plt.xlabel("C2A2")
plt.ylabel("Minimalna sigurna visina otvaranja (m)")
plt.title("Ovisnost o aerodinamičkom otporu")
plt.grid()
plt.show()

                


import numpy as np

#Parametri
g = 9.81
m = 80
rho = 1.225

# prije otvaranja
C1 = 1.0
A1 = 0.70
# nakon otvaranja
C2 = 1.5
A2 = 22.0

# terminalna brzina slobodnog pada
v_terminal = np.sqrt((2*m*g)/(rho*C1*A1))

print(f"Terminalna brzina = {v_terminal} m/s")

def max_G_pri_otvaranju(t_otv, dt=0.001):
    v = v_terminal
    max_G = 0
    t = 0

    while t <= t_otv:
        faktor = t / t_otv
        CA = (C1*A1) + faktor*((C2*A2) - (C1*A1))
        F = 0.5 * rho * v**2 * CA
        a = g - F/m
        G = abs(a)/g

        if G > max_G:
            max_G = G
        v += a*dt
        t += dt

    return max_G


print("Vrijeme otvaranja (s)   Maksimalna G-sila:")
for t_otv in [0.1, 0.5, 1.0, 2.0, 3.0, 4.0]:
    Gmax = max_G_pri_otvaranju(t_otv)
    print(f"{t_otv} {Gmax}")

#Ovaj kod postavljamo kako bi dokazali da prepostavljeno postupno otvaranje padobrana od 3 sekunde u našem orginalnom programu stvara podnošljive G-sile s našim trenutnim parametrima.
#Također pokazuje da je naglo otvaranje od manje od jedne sekunde previše štetno ljudskom skakaču te zbog toga nagla otvarnja u ostalim programima možemo zanemariti.

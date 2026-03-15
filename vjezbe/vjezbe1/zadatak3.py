try:
    x1 = float(input("Unesite x koordinatu 1.točke: "))
except ValueError:
    print("Upozorenje: unesena vrijednost nije broj! Koristi se default = 0")
    x1 = 0
try:
    y1 = float(input("Unesite y koordinatu 1.točke: "))
except ValueError:
    print("Upozorenje: unesena vrijednost nije broj! Koristi se default = 0")
    y1 = 0
try:
    x2 = float(input("Unesite x koordinatu 2.točke: "))
except ValueError:
    print("Upozorenje: unesena vrijednost nije broj! Koristi se default = 1")  # default 1 da ne dijeli s nulom
    x2 = 1
try:
    y2 = float(input("Unesite y koordinatu 2.točke: "))
except ValueError:
    print("Upozorenje: unesena vrijednost nije broj! Koristi se default = 0")
    y2 = 0
if x2 == x1:
    print("x1 i x2 ne smiju biti jednaki!")
m = (y2 - y1)/(x2 - x1)
c = y2 - m*x2
print (f"y = {m}x + {c}")
#Ai je pomogao za obavijest prilikom pogreške unosa koordinata.
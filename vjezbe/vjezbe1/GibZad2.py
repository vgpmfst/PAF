import kinematika as kin

masa = float(input("Unesite masu čestice u kg: "))
sila = float(input("Unesite silu koja djeluje na česticu: "))

kin.jednoliko_gibanje(F=sila, m=masa)
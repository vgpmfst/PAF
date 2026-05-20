import numpy as np
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0,scale=0.2,size=10000)

def funkcija(podaci):
    n = len(podaci)

    # srednja vrijednost
    x = np.mean(podaci)

    # standardna devijacija s dijeljenjem s n
    sigma_n = np.std(podaci) 

    # standardna devijacija s dijeljenjem s n-1
    s = np.std(podaci, ddof=1)#ddof u numpy određuje s čime se dijeli pri računanju standardne devijacije

    # standardna pogreška srednje vrijednosti
    sigma_x = s / np.sqrt(n)

    # relativna razlika između sigma_n i s
    rel_razlika = abs(s - sigma_n) / sigma_n * 100

    print("Broj mjerenja:",n, "Srednja vrijednost:",x,"σ_n:",sigma_n,"s:",s,"σ_x:",sigma_x,"Relativna razlika između σ_n i s:",rel_razlika)
    return (n, x, sigma_n, s, sigma_x, rel_razlika)

rezultati_malo = funkcija(malo_n)
rezultati_veliko = funkcija(veliko_n)

#a s ostaje približno konstantan kada povećamo broj mjerenja a σ_x se smanjuje približno kao 1 kroz korijen n.
#b Relativna razlika između σ_n i s je velika za mali uzorak a skoro nestaje za veliki uzorak.
#c np.std() standardno koristi ddof=0 i dijeli s n a to je ispravno kada imamo cijelu populaciju podataka. Za uzorak koristimo ddof=1.

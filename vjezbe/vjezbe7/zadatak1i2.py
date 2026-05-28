import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np.random.normal( loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]

def histogram(podaci, k):
    h = (max(podaci)-min(podaci))/k
    rubovi = []
    frekvencije = []
    for i in range(k):
        donji_rub = min(podaci) + i*h
        gornji_rub = donji_rub + h
        rubovi.append(donji_rub)
        if i == k - 1:
            broj = sum(donji_rub <= x <= gornji_rub for x in podaci)
        else:
            broj = sum(donji_rub <= x < gornji_rub for x in podaci)
        frekvencije.append(broj)
        print(f"[{donji_rub}, {gornji_rub}: {broj}")
    return rubovi,frekvencije,h
    
k = 10
rubovi,frekvencije,h = histogram(mase_ciste,k)

plt.bar(rubovi, frekvencije, width=h, bottom=None, align="edge",edgecolor="black")
plt.xlabel("Mase")
plt.ylabel("Frekvencija")
plt.title("Histogram")
plt.tight_layout()
plt.show()



plt.hist(mase_ciste,bins=10,edgecolor="black")
plt.axvline(np.mean(mase_ciste), color='k', linestyle='dashed', linewidth=1)
plt.axvline(np.median(mase_ciste),color = "red",linestyle = "dashed",linewidth = 1)
plt.xlabel("Mase")
plt.ylabel("Frekvencija")
plt.title("Histogram")
plt.show()
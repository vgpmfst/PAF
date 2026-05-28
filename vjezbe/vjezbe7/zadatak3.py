import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np.random.normal( loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]

a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6] # paran n
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5] # neparan n

def medijan(podaci):
    podaci = sorted(podaci)
    i = len(podaci)/ 2-1 # -1 se dodaje zbog pomaka indeksiranja od nule
    if i % 1:
        print(podaci[int(i) + 1])
        return podaci[int(i) + 1]
    else:
        print((podaci[int(i)] + podaci[int(i) + 1]) / 2)
        return (podaci[int(i)] + podaci[int(i) + 1]) / 2
    
medijan(a)
medijan(b)
medijan(mase)

print(np.median(a))
print(np.median(b))
print(np.median(mase))
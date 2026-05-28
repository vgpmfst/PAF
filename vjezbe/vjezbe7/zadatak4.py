import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np.random.normal( loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]
                     
sredina = np.mean(mase)
medijan = np.median(mase)

print("Aritmetička sredina:", np.mean(mase))
print("Medijan:", np.median(mase))
print(f"Razlika{abs((np.mean(mase))-np.median(mase))}")

mase = np.array(mase)

q1 = np.percentile(mase, 25)
q3 = np.percentile(mase, 75)
iqr = q3 - q1

gornja_granica = q1 + 1.5 * iqr
donja_granica = q3 - 1.5 * iqr

mase_filtrirane = mase[(mase >= donja_granica) &(mase <= gornja_granica)]

sredina_filtriran = np.mean(mase_filtrirane)
medijan_filtriran = np.median(mase_filtrirane)
print("Sredina podataka bez odstupanja:", sredina_filtriran)
print("Medijan podataka bez odstzpanja:", medijan_filtriran)
print("Razlika podataka bez odstupanja:", abs(sredina_filtriran-medijan_filtriran))

plt.hist(mase, bins=20, color='lightblue', edgecolor='black')
plt.axvline(sredina, color="red", linestyle="--",label="sredina")
plt.axvline(medijan, color="blue", linestyle="--",label="medijan")
plt.axvline(sredina_filtriran,color="yellow",linestyle="-",label="sredina_filtriran")
plt.axvline(medijan_filtriran,color="green",linestyle="-",label="medijan_filtriran")
plt.xlabel("Mase")
plt.ylabel("Frekvencija")
plt.title("Histogram")
plt.legend()
plt.show()
import math
#aritmetička sredina
def aritm_sredina(n,xi):
  x = 0
  for i in range(n):
    x += xi[i]
  print(x/n) 
  return(x/n)
vrijednosti = [1,2,3,4,5,6,7,8,9,10]
aritm_sredina(10,vrijednosti)
#standardna devijacija
def standardna_devijacija(n,xi):
  x = 0
  t = 0 
  for i in range(n):
    x += xi[i]
  srednja = x/n
  for i in range(n):
    t += (xi[i]- srednja )**2
  σ = math.sqrt(t/(n-1))
  print(σ)
  return(σ)
standardna_devijacija(10,vrijednosti)
  

#Explain your work

#Question 1
import math
import random

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return n>1;
primeList=[2]
for n in range(3, 1000):
    if isPrime(n):
        primeList.append(n)

matris = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
for i in range(3):
  for j in range(3):
    tutulanSayi=random.randint(0,len(primeList)-1)
    matris[i][j]=primeList[tutulanSayi]
    primeList.pop(tutulanSayi)
print(matris)

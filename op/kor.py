#kor
from doctest import master
import math
import random

class Kor:
    def __init__ (self,sugar,kozeppont = (0,0)):
        self.kozeppont = kozeppont
        self.sugar = sugar

    def terulet(self):
        return self.sugar*math.pow(math.pi,2)

    def kerulet(self):
        return self.sugar*2*math.pi

    def info(self):
        print(f'A(z) {self.sugar} egység sugarú, {self.kozeppont} középpont kör területe  {self.terulet():.2f}egység, kerülete {self.kerulet():.2f} egység ')

#példány
kor_01 = Kor(5,(2,6))

#Tesztelés
#print(kor_01)
print(type(kor_01))
print(isinstance(kor_01,Kor))

# metodus
print(kor_01.terulet())

korok = []

for _ in range(5):
  kor = Kor(random.randint(0,10))
  korok.append(kor)

for kor in korok:
    kor.info()
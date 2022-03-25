#pontszam = int(input('Kérem a pontszámát!:'))
#nev = input('Kérem a nevét!:')

""""
if pontszam >= 48:
    print('vizsgája sikeres')
elif pontszam == 48:
    print('szerencséje van')
else:
    print('vizsgája sikertelen')
"""
from sqlalchemy import true


def sikeres():
    if pontszam >= 48:
        return f'vizsgája sikeres'
    elif pontszam == 48:
        return f'szerencséje van'
    else:
        return f'vizsgája sikertelen'

nev = None
while nev != '':
    nev = input('Kérem a nevét!:')
    if nev:
        pontszam = int(input('Kérem a pontszámát!:'))
        if sikeres():
            print(nev,'vizsgája sikeres')
        else:
            print(nev,'vizsgája sikertelen')

class Vizsgázó():
    def __init__(self,nev,pont):
        self.nev = input('Adja meg a nevet!:')
        self.pont = int(input('Adja meg a pontszamot'))
    def sikeres(self):
        if self.pont >= 48:
            return True
        else:
            return False
diak = Vizsgázó()
print(diak.sikeres())
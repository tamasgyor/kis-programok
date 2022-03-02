nev = None


def siker(pontszam):
    if pontszam >= 48:
        return  True
    else:
        return  False


while nev != '':
    nev = input('Kérem a nevét!')
    if nev:
        pontszam = int(input('Kérem a pontszámát!'))
        if siker(pontszam):
          print(f'{nev} vizsgája sikeres')
        else:
            print('vizsgája sikertelen')

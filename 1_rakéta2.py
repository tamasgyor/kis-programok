indul = int(input('Hány órás a visszaszámlálás'))
felfüggesztés = 0

for szam in range(indul,0,-1):
    print('visszaszámlálás',szam)
    valasz = input('Fel kell e függeszteni (i/n)')
    if valasz =='i':
        felfüggesztés +=1
print('a rakéta a visszaszámlálást követően ennyi órával indult:', indul + felfüggesztés)
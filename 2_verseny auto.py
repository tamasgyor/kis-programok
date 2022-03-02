auto_tipus = input('Adja meg az autó típusát')
ev = int(input('Adja meg a gyártási évet'))
sebesseg = int(input('Adja meg a sebességet'))


if auto_tipus[0] == 'A' or auto_tipus[0] == 'B':
    print('Német auto')
else: 
    print('Ismeretlen')
if ev >= 2001:
    print('XXI. század')
elif ev <= 2000:
    print('XX. század')
elif ev == 2022:
    print('Mostani')
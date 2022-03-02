szó1 = input('Adjon meg egy szót:')
szó2 = input('Adjon meg egy szót:')

if len(szó1) > len(szó2):
    print('Az első szó hosszabb')
elif len(szó1) < len(szó2):
    print('Az első szó rövidebb')
else:
    print('a két szó egyforma hosszú')
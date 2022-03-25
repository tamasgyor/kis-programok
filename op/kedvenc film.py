def oraperc():
    return str(ora) + 'ora' + str(perc) + 'perc'

def oraperc(perc):
    ora = percek//60
    perc = percek- ora * 60
    return str(ora) + 'ora' + str(perc) + 'perc'

for _ in range(3):
    cim = input('kérem addjon meg egy filmet')
    hossz = int(input('kérem addja meg a film hosszát'))
    print('A(z) cím'cím film',oraperc(hossz),'hosszú')
    print(f'A(z) cím'cím film',oraperc(hossz),'hosszú')
wr = open('bolt.txt','w')
def hanyora(ora):
    if ora >= 8 and ora <= 16:
        return f'a bolt nyitva van'
    else:
        return f'A bolt nincs nyitva'

ora = int(input('Hány óra van ?:'))
print(hanyora(ora))
wr.write(f'{ora}:óra van\n')
wr.write(f'{hanyora(ora)}')
wr.close()
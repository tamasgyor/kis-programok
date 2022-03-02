model = input('kérem a model nevét!')
kor = int(input('kérem az életkorát!'))
magassag = int(input('Kérem a magasságot!'))
if kor < 20:
    print(f'{kor}:csitri')
elif kor == 20:
    print(f'{kor}:lkalmazható')
else:
    print(f'{kor}:vén')

if magassag >= 170 and magassag <= 170:
    print(f'{magassag}:pont jó')
else:
    print(f'{magassag}:nem jó')
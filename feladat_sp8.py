szam=int(input('Kérek egy egész számot! '))

if szam%3 ==0:
    print(f'Ez a szám 3-mal osztható, {szam}.')

if szam%4 ==0:
    print(f'Ez a szám 4-gyel osztható, {szam}.')
    
if szam%4 ==0 and szam%3 ==0:
    print(f'Ez a szám 4-gyel és 3-mal osztható, {szam}.')

else:
    print(f'Ez a szám nem osztható 4-gyel se 3-mal, {szam}.')
import random as rnd

# feltöltünk egy 10 elemű listát 2 számjegyű véletlen számokkal
szamok:list[int] = []
for x in range(10):
    sz:int = rnd.randint(10, 99)
    szamok.append(sz)

# kiírás:
print(f'a lista elemei: {szamok}')

# meghatározzuk a számok összegét
# [vagyis alkalmazzuk a sorozatszámítás tételét összeadásra]
osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'számok összege: {osszeg}')

# meghatározzuk a páros számok darabszámát:
# [vagyis alkalmazzuk a megszámlálás tételét]
szamlalo:int = 0
for szam in szamok:
    if szam % 2 == 0:
        szamlalo += 1
print(f'páros számok száma: {szamlalo}')

# meghatározzuk a legnagyobb szám helyét és értékét:
# [szélsőérték - maximum]
maxi = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i
print(f'a legnagyobb szám a {szamok[maxi]}, indexe: {maxi}')

# meghatározzuk a legkisebb szám helyét és értékét:
# [szélsőérték - miminum]
mini = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[mini]:
        mini = i
print(f'a legkisebb szám a {szamok[mini]}, indexe: {mini}')

# bekérek egy számot, és megállapítom, hogy szerepel-e a listában, vagy sem
# [eldöntés tételének alkalmazása]
eld:int = int(input('szám eldöntéshez: '))

i:int = 0
while i < len(szamok) and szamok[i] != eld:
    i += 1
if i < len(szamok): print(f'benne van a(z) {eld}')
else: print(f'nincs benne {eld}')

# bekérek egy számot, és megmondom, hogy mi az indexe, HA benne van
# HA nincs benne, akkor pedig kiírom, hogy 'nincs benne'
ker:int = int(input('szám kereséshez: '))
i:int = 0
while i < len(szamok) and szamok[i] != ker:
    i += 1
if i < len(szamok): print(f'a {ker} érték indexe a listában {i}')
else: print(f'nencs benne {ker}')

# !!!kiválasztás tételét CSAK olyan elemre alkalmazhatunk, ami BIZTOSAN benne van a sorozatban
# bekérünk egy számot (ami szerepel a sorozatban), visszadjuk az indexét:
kiv:int = int(input('szám kiválasztáshoz: '))
i:int = 0
while szamok[i] != kiv:
    i += 1
print(f'a {kiv} indexe: {i}')
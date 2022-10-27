# ún. "homogén" listák:
szamok = [42, 11, 31, 10, 9, 71, 11]

# lehet ilyet, de most inkább ne...:
# ún. "heterogén" lista
vegyes = [31, 'cica', 3.14, True]

print(f'lista elemei: {szamok}')

uj_szam:int = int(input('új szám: '))
# elem hozzáadása a lista végéhez:
szamok.append(uj_szam)
print(f'lista elemei: {szamok}')

# lista hossza:
lista_hossza:int = len(szamok)
print(f'lista elemeinek száma: {lista_hossza}')

torlendo:int = int(input('mit szeretnél törölni?: '))
# remove: törli az első olyan elemet, aminek az értéke azonos a paraméterrel
szamok.remove(torlendo)
print(f'lista elemei: {szamok}')

# i:int = 0
# while i < len(szamok):
#     if szamok[i] == torlendo:
#         szamok.pop(i)
#     else: i += 1

print(f'a lista 3mas indexű eleme: {szamok[3]}')
szamok[3] = int(input('3mas indexű elem új értéke: '))
print(f'lista elemei: {szamok}')

# a lista elemei "indexelve" vannak,
# ez annyit jelent, hogy minden elemhez tartozik egy "sorszám"
# "zero based index"
# konkrét elemre tehát így hivatkozunk:
# <lista_neve>[<elem_indexe>]

# <lista_neve>.pop(<index>) -> eltávolítja az adott indexedik elemet

zoldsegek = ['répa', 'retek', 'káposzta', 'paprika']

# lista utolsó eleme
print(zoldsegek[-1])

# 1es indexűtől a 3mas indexűig (zárt -> nyílt)
print(zoldsegek[1:3])

# 1es indexű elemtől a végéig
print(zoldsegek[1:])

# 2es indexű elemig
print(zoldsegek[:2])

# <lista_neve>.insert(<hová>, <mit>)
zoldsegek.insert(2, "krumpli")
print(zoldsegek)
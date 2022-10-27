nevek = ['Ferenc', 'Péter', 'Kata', 'Klára', 'Zoltán', 'Lukrécia']

for i in range(len(nevek)):
    # így működik:
    # nevek[i] = 'új érték'
    print(f'{i}. indexű elem: {nevek[i]}')

for nev in nevek:
    # ez hülyeség: 
    # nev = 'valami más'
    print(nev)

print(nevek)
i:int = 0
while i < len(nevek):
    print(nevek[i])
    i += 1

eddig:str = input('meddig nézzük a neveket?: ')

# i:int = 0
# while i < len(nevek) and nevek[i] != eddig:
#     print(nevek[i])
#     i += 1


# !!!csak python!!!
# a "ciklus else ága" akkor fut le, ha a ciklus futása alatt sosem volt break:

i:int = 0
while i < len(nevek):
    print(nevek[i])
    if nevek[i] == eddig: break
    i += 1
else: print(f'nem volt {eddig}')

for nev in nevek:
    if nev == eddig: break
else: print(f'nem volt {eddig}')
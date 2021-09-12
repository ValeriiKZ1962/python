
spisok = ['H', 'e', 'l', 'l', 'o']
if len(spisok) % 2 == 0:
    i = 0
    while i < len(spisok):
        a = spisok[i]
        spisok[i] = spisok[i+1]
        spisok[i+1] = a
        i = i + 2
else:
    i = 0
    while i < len(spisok) - 1:
        a = spisok[i]
        spisok[i] = spisok[i + 1]
        spisok[i + 1] = a
        i = i + 2
print(spisok)

input()


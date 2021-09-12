my_stroke = input('Введите строку ')
a = my_stroke.split()
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i}.  {el}')


# Реализовать два небольших скрипта:
# 1) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# Подсказка: использовать функцию count() и cycle() модуля itertools

def gen():
    a = int(input('Введите начальное число: '))
    from itertools import islice
    from itertools import count
    for i in islice(count(a), 15):
        print(i)
gen()

# 2) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее

def gen():
    list = [99, None, "my_list", 3]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 6):
        print(el)
gen()


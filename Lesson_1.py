# Пример 1

name = input('Ваше имя? ')
print(name,', добро пожаловать')
num_1 = int(input('введи 1 '))
num_2 = int(input('введи 2 '))
print(num_1 + num_2)

# Пример 2

sec = int(input('Время в секундах '))
hour = int(sec // 3600)
min = int(sec % 3600 // 60)
sec = int(sec % 3600 % 60)
print(f'{hour}:{min}:{sec}')

# Пример 3

n = int(input('Введи целое число '))
print(n + (n * 10 + n) + (n * 100 + n * 10 + n))

# Пример 4

n = int(input('Введи целое положительное число '))
a = n % 10
n = n // 10
while n > 0:
    if n % 10 > a:
        a = n % 10
    n = n // 10
print(a)

# Пример 5

income = float(input('Сообщите выручку '))
expences = float(input('Сообщите издержки '))
profit = income - expences
print(profit)
if profit >= 0:
    profitability = profit / income * 100
    print(profitability)
    n_stuff = int(input('Введите число сотрудников '))
    profit_per_employee = (profitability / n_stuff)
    print(profit_per_employee)

# Пример 6

a = float(input('Введи результат пробежки в 1 день в км '))
b = float(input('Введи желаемый результат пробежки в км '))
n = 1
while a * (1.1 ** n) < b:
    n = n + 1
else:
    print(f'на {int(n + 1)} день спортсмен достиг результата - не менее {b} км.')

input()



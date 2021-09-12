num = int(input('Введите число'))
random_list = [7, 4, 3, 2]
i = 0
for n in random_list:
    if num <= n:
        i += 1
    elif num > n:
        break
random_list.insert(i, float(num))
print(random_list)


def my_func(a, b, c):
    my_set = [a, b, c]
    total = []
    max_1 = max(my_set)
    total.append(max_1)
    my_set.remove(max_1)
    max_2 = max(my_set)
    total.append(max_2)
    print(sum(total))

my_func(8, -3, 0)

input()

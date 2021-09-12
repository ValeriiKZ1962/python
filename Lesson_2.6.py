goods = []
features = {'название': '', 'цена': '', 'количество': '', 'ед.изм.': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед.изм.': []}
num = 0
while True:
    if input('Выход Q, продолжить Enter').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        prop = input(f'введите значение свойства {f}')
        features[f] = int(prop) if (f == 'цена' or f == 'количество') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\nТекущая аналитика по товарам\n{'*' *30}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
        print('*' * 30)

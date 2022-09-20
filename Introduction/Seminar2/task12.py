n = int(input('Введите значение n, т.е. кол-во элементов словаря: '))
d : dict = dict(enumerate([(x + 1) * 3 + 1 for x in range(n)], start=1))
print(f'Получившийся словарь: {d}')
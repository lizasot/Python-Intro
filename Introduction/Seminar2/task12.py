n = int(input('Введите значение n, т.е. кол-во элементов словаря: '))

d : dict = {}

for x in range(n):
    d[x + 1]  = (x + 1) * 3 + 1
print(f'Получившийся словарь: {d}')
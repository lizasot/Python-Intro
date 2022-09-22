l = list(map(int, input('Введите через пробел числа: ').split()))
result : list = []

for x in range(0,len(l)):
    if l[x] not in result:
        result.append(l[x])

print(f'{l} => {result}')

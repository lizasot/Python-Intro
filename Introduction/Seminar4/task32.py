l = list(map(int, input('Введите через пробел числа: ').split()))
result : list = []
print(f'{l} => ', end='')

l.sort()
for x in range(0,len(l)):
    if not (l[x] == l[x-1] or (x != len(l) -1 and l[x] == l[x+1])):
        result.append(l[x])

print(f'{result}')
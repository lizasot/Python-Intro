l = list(map(int, input('Введите через пробел числа: ').split()))
result : list = []
print(f'{l} => ', end='')

check = lambda x: True if not (l[x] == l[x - 1] or (x != len(l) -1 and l[x] == l[x + 1])) else False

l.sort()
result = [l[x] for x in range(0,len(l)) if check(x)] 

print(f'{result}')
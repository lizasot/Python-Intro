l = list(map(int, input('Введите через пробел числа: ').split()))

max_numb = l[0]
min_numb = l[0]

for x in range(len(l)):
    if min_numb > l[x]:
        min_numb = l[x]
    if max_numb < l[x]:
        max_numb = l[x]

print(f'Наибольшее число: {max_numb}')
print(f'Наименьшее число: {min_numb}')
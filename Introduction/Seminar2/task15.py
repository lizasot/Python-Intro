n = int(input('Введите число N: '))
res_list : list = []

for x in range(1,n+1):
    if x == 1:
        res_list.append(1)
    else:
        res_list.append(res_list[x - 2] * x)

print(res_list)
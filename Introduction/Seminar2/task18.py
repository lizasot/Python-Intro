from random import randint

n = int(input('Введите количество элементов в списке: '))

numb_list : list =  []
for x in range(1,n+1):
    numb_list.append(x)

print(numb_list)
res_list : list =  []

for x in range(0,n):
    ind = randint(0,len(numb_list) - 1)
    res_list.append(numb_list[ind])
    numb_list.pop(ind)
print(res_list)
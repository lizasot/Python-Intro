n = int(input('Введите число N: '))

numb_list : list =  []
for x in range(-n,n+1):
    numb_list.append(x)

result = 0

with open('file.txt') as f:
    result = numb_list[int(f.readline())] * numb_list[int(f.readline(2))]
print(result)
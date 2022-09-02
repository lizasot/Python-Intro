def factorial(n : int):
    result = 1
    for x in range(2,n+1):
        result*=x
    return result

n = int(input('Введите число N: '))
res_list : list = []

for x in range(1,n+1):
    res_list.append(factorial(x))

print(res_list)
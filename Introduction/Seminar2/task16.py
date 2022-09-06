def calculate(n : int):
    result = (1 + 1/n)**n
    return result

n = int(input('Введите число N: '))
summ = 0

for x in range(1,n+1):
    summ += calculate(x)

print(summ)
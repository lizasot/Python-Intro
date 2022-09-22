from functools import reduce
n = int(input('Введите число N: '))
summ = reduce(lambda x, y: x + y, [(1 + 1 / n) ** n for n in range(1, n + 1)])
print(summ)
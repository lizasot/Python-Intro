from functools import reduce

def calculate(n : int):
    result = (1 + 1/n)**n
    return result

n = int(input('Введите число N: '))
summ = reduce(lambda x, y: x + y, [(1 + 1/n)**n for n in range(1, n + 1)])

print(summ)
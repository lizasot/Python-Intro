def multiplyPairs(l:list):
    result : list = []
    for x in range(0,round(len(l) / 2 + 0.1)):
        result.append(l[x]*l[(len(l) - 1) - x])
    return result

l = list(map(int, input('Введите через пробел числа: ').split()))
test_l : list = [2, 3, 4, 5, 6]

print(f'Ваш список чисел: {l}')
print(f'Произведение пар чисел вышего списка: {multiplyPairs(l)}')

print(f'Тестовый список чисел: {test_l}')
print(f'Произведение пар чисел тестового списка: {multiplyPairs(test_l)}')
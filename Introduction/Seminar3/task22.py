def summOddPos(l:list):
    result = 0
    for x in range(1,len(l), 2):
        result += l[x]
    return result

l = list(map(int, input('Введите через пробел числа: ').split()))
test_l : list = [2, 3, 5, 9, 3]

print(f'Ваш список чисел: {l}')
print(f'Сумма чисел вашего списка на нечётных позициях: {summOddPos(l)}')

print(f'Тестовый список чисел: {test_l}')
print(f'Сумма чисел тестового списка на нечётных позициях: {summOddPos(test_l)}')
from functools import reduce

numb = input('Введите число: ')

to_int = lambda x: int(x) if x.isdigit() else 0
summ = reduce(lambda x, y: x + y, [to_int(n) for n in numb])

print(f'Сумма всех цифр в числе: {summ}')
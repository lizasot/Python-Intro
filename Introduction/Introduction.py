# -*- coding: cp1251 -*-
print('Введите номер четверти прямоугольной системы координат: ')
quarter = input()

print('Допустимые значения: ')
if ('3' in quarter) or ('III' in quarter):
    print('x < 0; y < 0')
elif ('2' in quarter) or ('II' in quarter):
    print('x < 0; y > 0')
elif ('1' in quarter) or ('I' in quarter):
    print('x > 0; y > 0')
elif ('4' in quarter) or ('IV' in quarter):
    print('x > 0; y < 0')
elif x == 0 and y != 0:
    print('Ошибка! Неудалось распознать введённую четверть.')
# -*- coding: cp1251 -*-
x = float(input('x = '))
y = float(input('y = '))

if x > 0 and y > 0:
    print('I ��������')
elif x < 0 and y > 0:
    print('II ��������')
elif x < 0 and y < 0:
    print('III ��������')
elif x > 0 and y < 0:
    print('IV ��������')
elif x == 0 and y != 0:
    print('��� Y')
elif x != 0 and y == 0:
    print('��� X')
elif x == 0 and y == 0:
    print('�����')
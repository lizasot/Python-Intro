# -*- coding: cp1251 -*-
print('������� ���������� ������ �����: ')
x1 = float(input('x = '))
y1 = float(input('y = '))
z1 = float(input('z = '))
print('������� ���������� ������ �����: ')
x2 = float(input('x = '))
y2 = float(input('y = '))
z2 = float(input('z = '))

print('���������� ����� ����� ��������� �������: ')
print(round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** (0.5),3))
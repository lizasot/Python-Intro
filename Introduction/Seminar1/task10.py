print('Введите координаты первой точки: ')
x1, y1, z1 = list(map(float, input('Введите через пробел координаты первой точки (x,y,z): ').split()))
x2, y2, z2 = list(map(float, input('Введите через пробел координаты второй точки (x,y,z): ').split()))

print('Расстояние между двумя точками пространства: ')
print(round(((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** (0.5),3))
def getStrSummPoly(poly1 : str, poly2 : str):
    dict_args : dict = {}
    for x in range(0,len(poly1)):
        if poly1[x] == '*':
            y = x
            while y != 0 or poly1[y] != ' ':
                y -= 1
            y += 1
            key = int(poly1[y:x])

with open('polynomial1.txt','r') as p1, open('polynomial2.txt','r') as p2:
    poly1 = p1.read()
    poly2 = p2.read()
print(f'Первый многочлен: {poly1}')
print(f'Второй многочлен: {poly2}')
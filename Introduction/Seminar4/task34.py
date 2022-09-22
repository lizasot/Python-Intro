def getIntArg(member : str):
    if member[0] == 'x':
        return 1
    elif member[0].isdigit():
        y = 0
        while y != (len(member) - 1) and member[y] != '*':
            y+= 1
        if y == (len(member) - 1):
            return int(member[:])
        else:
            return int(member[:y])
    else:
        return 0

def getIntDegree(member : str):
    y = 0
    while y != (len(member) - 1) and member[y] != '^':
        y+= 1
    y += 1
    if y != len(member):
        return int(member[y:])
    elif member[y-1] == 'x':
        return 1
    else:
        return 0

def getStrPolyFromDict(dict_args : dict):
    result = ''
    # dict_args = dict(sorted(dict_args.items(), reverse=True))
    for x in dict(sorted(dict_args.items(), reverse=True)).keys():
        if x > 1 and dict_args[x] > 1:
            result += str(dict_args[x])
            result += '*x^'
            result += str(x)
        elif x == 1 and dict_args[x] > 1:
            result += str(dict_args[x])
            result += '*x'
        if x != 0:
            result += ' + '
        else:
            result += str(dict_args[x])
    result += '\n'
    return result

def getStrSummPoly(poly1 : str, poly2 : str):
    dict_args : dict = {}
    y = 0
    for x in range(0,len(poly1)):
        if poly1[x] == ' ' or poly1[x] == '\n':
            member = poly1[y:x]
            if member != '+':
                key = getIntDegree(poly1[y:x])
                value = getIntArg(poly1[y:x])
                dict_args[key] = value
            y = x + 1
    y = 0
    for x in range(0,len(poly2)):
        if poly2[x] == ' ' or poly2[x] == '\n':
            member = poly2[y:x]
            if member != '+':
                key = getIntDegree(poly2[y:x])
                value = getIntArg(poly2[y:x])
                if key in dict_args.keys():
                    dict_args[key] += value
                else:
                    dict_args[key] = value
            y = x + 1
    return getStrPolyFromDict(dict_args)

#Выражения должны быть записаны в том же формате, как их записывает задача 33
with open('polynomial1.txt','r') as p1, open('polynomial2.txt','r') as p2:
    poly1 = p1.read()
    poly2 = p2.read()

#print(f'Первый многочлен: {poly1}')
#print(f'Второй многочлен: {poly2}')
#print(f'Их сумма: {getStrSummPoly(poly1,poly2)}')

with open('polynomial3.txt','w') as f:
    f.write(getStrSummPoly(poly1,poly2))
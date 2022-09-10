from random import randint

def getStrAXK(a : int, k : int):
    if a == 0:
        return ''
    if a != 1 and k != 0:
        result = (f'{a}*')
    elif a != 1:
        result = (f'{a}')
    else:
        result = ''
    if k > 1:
        result += (f'x^{k}')
    elif k == 1:
        result += 'x'
    return result

k = int(input('Введите число k, обозначающее степень многочлена: '))

with open('polynomial.txt','w') as f:
    for x in range(k,-1,-1):
        res = getStrAXK(randint(0,100),x)
        if x != k and len(res) != 0:
            f.write(' + ')
        f.write(res)
    f.write('\n')
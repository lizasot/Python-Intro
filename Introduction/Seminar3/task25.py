def fromDecimalToBinary(numb : int):
    result : list = []
    while (numb > 2):
        result.append(numb % 2)
        numb = int(numb / 2)
    result.append(1)
    result.reverse()
    return ''.join(map(str,result))
numb = int(input('Введите десятичное число: '))
print(f'Двоичное число: {fromDecimalToBinary(numb)}')
def deleteABV(text : str):
    y = 0
    result = ''
    for x in range(0,len(text)+1):
        if x == len(text) or text[x] == ' ' :
            if 'абв' not in text[y:x]:
                result += text[y:x]
            y = x
    result = result.strip()
    return result

text = input('Введите текст: ')
print('Удаляются все слова, содержащие "абв"...')
print()

print('Получившийся текст:')
print(deleteABV(text))
print()
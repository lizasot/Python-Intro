def deleteABV(text : str):
    l = text.split()
    result: list = []
    for x in range(0,len(l)):
        if 'абв' not in l[x]:
            result.append(l[x])
    return ' '.join(result)

text = input('Введите текст: ')
print('Удаляются все слова, содержащие "абв"...')
print()

print('Получившийся текст:')
print(deleteABV(text))
print()
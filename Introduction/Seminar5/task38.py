text = input('Введите текст: ').split()
print('Удаляются все слова, содержащие "абв"...')
print()

print('Получившийся текст:')
print(' '.join(list(filter(lambda x: 'абв' not in x, text))))
print()
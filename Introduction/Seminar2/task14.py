numb = input('Введите число: ')

summ : int = 0

for x in range(0,len(numb)):
    if numb[x] == '.' or numb[x] == ',':
        pass
    if ord('0') < ord(numb[x]) <= ord('9'):
        summ += int(numb[x])

print(f'Сумма всех цифр в числе: {summ}')
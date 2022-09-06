main_str = input('Введите строку, в которой необходимо искать подстроку: ')
sub_str = input('Введите подстроку, которую необходимо найти: ')

start = 0
end = len(sub_str) - 1
matches = 0

while (end < len(main_str)):
    if sub_str == main_str[start:end + 1]:
        matches += 1
    start += 1
    end += 1

print(f'Найдено совпадений: {matches}')
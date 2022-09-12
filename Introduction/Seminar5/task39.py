while True:
    k = int(input('Введите изначальное количество конфет: '))
    if k > 0:
        break

while True:
    max_take = int(input('Введите максимальное количество конфет, которое можно взять за ход: '))
    if max_take > 0:
        break

end_game = False
current_player = False

while end_game == False:
    print(f'Текущее количество конфет: {k}')
    current_max_take = min(max_take,k)
    if current_player:
        print('Ходит игрок 2')
    else:
        print('Ходит игрок 1')

    if current_max_take == 1:
        print(f'Можно взять конфет: {current_max_take}')
    else:
        print(f'Можно взять конфет: 1-{current_max_take}')

    while True:
        take = int(input('Сколько взять конфет: '))
        if take > 0 and take <= current_max_take:
            break

    k -= take
    if k == 0:
        end_game = True
    else:
        current_player = not current_player

if current_player:
    print('Победил игрок 2')
else:
    print('Победил игрок 1')
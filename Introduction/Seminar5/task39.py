from random import randint

def generateTakenCandy(max_take : int, candy : int):
    if candy - max_take <= 0:
        return min(max_take, candy)

    #candy - x = (max_take + 1)
    #candy - (max_take + 1) = x
    if (candy - (max_take*2) <= 0):
        return candy - (max_take + 1)
    else:
        return randint(1, max_take)
def startGameConsole(mode : int = 1, candy = 30, max_take = 3):
    end_game = False
    current_player = False

    while end_game == False:
        print()
        print(f'Текущее количество конфет: {candy}')
        current_max_take = min(max_take, candy)
        if current_player:
            print('##Ходит игрок 2')
        else:
            print('#Ходит игрок 1')

        if current_max_take == 1:
            print(f'Можно взять конфет: {current_max_take}')
        else:
            print(f'Можно взять конфет: 1-{current_max_take}')

        while True:
            if current_player and mode > 1:
                if mode == 2:
                    take = randint(1,current_max_take)
                    print(f'Игрок 2 забирает конфет: {take}')
                    break
                else:
                    take = generateTakenCandy(current_max_take,candy)
                    print(f'Игрок 2 забирает конфет: {take}')
                    break
            else:
                take = int(input('Сколько взять конфет: '))
                if take > 0 and take <= current_max_take:
                    break

        candy -= take
        if candy == 0:
            end_game = True
        else:
            current_player = not current_player

    if current_player:
        print('Победил игрок 2')
    else:
        print('Победил игрок 1')

        
print('[1] Игрок VS Игрок')
print('[2] Игрок VS Бот')
print('[3] Игрок VS Умный бот')
mode = int(input('Выберете режим игры (введите "1", "2" или "3"): '))


while True:
    k = int(input('Введите изначальное количество конфет: '))
    if k > 0:
        break

while True:
    max_take = int(input('Введите максимальное количество конфет, которое можно взять за ход: '))
    if max_take > 0:
        break
    
if mode == 1 or mode == 2 or mode == 3:
    startGameConsole(mode, k, max_take)
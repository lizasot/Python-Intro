from time import sleep
import keyboard

def getStrField(field : list):
    if len(field) != 9:
        return ''
    result = ''
    for x in range(0,9,3):
        result += f'{field[x+0]}|{field[x+1]}|{field[x+2]}\n'
    return result

def checkWin(field : list):
    #по горизонтали
    for x in range(0,9,3):
        if field[x+0]!= ' ' and field[x+1]!= ' ' and field[x+2] != ' ':
            return True
    #по вертикали
    for x in range(0,3):
        if field[x+0]!= ' ' and (field[x+3] == field[x+6]):
            return True
    #по диагонали
    if field[0] != ' ' and (field[0] == field[4] == field[8]):
        return True
    if field[2] != ' ' and (field[2] == field[4] == field[6]):
        return True
    return False

def drawSelectCell(field : list, ind : int):
    if len(field) != 9:
        return ''
    if ind < 0 or ind >= 9:
        return ''
    new_field = field
    new_field[ind] = '*'
    return getStrField(new_field)

def getIndFirstFreeCeil(field : list):
    for x in range(0,len(field)):
        if field[x]:
            return x
    return -1

field : list = [' ']*9
player = False

while True:
    if player:
        print('Ходит игрок 2') #'o'
    else:
        print('Ходит игрок 1') #'x'
    current_cell = getIndFirstFreeCeil(field)
    print(drawSelectCell(field,current_cell))
    key = keyboard.read_key()
    keyboard.on_release_key(key, callback)
    while key != 'enter':
        if key == 'left':
            print('press left')
        elif key == 'right':
            print('press right')
        elif key == 'up':
            print('press up')
        elif key == 'down':
            print('press down')
        key = keyboard.read_key()

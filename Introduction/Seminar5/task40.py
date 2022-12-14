from time import sleep
import keyboard, enum, os

def clear():
    #os.system('cls' if os.name=='nt' else 'clear')
    print('\n' * 100)

class Direction (enum.Enum):
    left = 1
    right = 2
    up = 3
    down = 4

def getStrField(field : list):
    if len(field) != 9:
        return ''
    result = ''
    for x in range(0, 9, 3):
        result += f'{field[x+0]}|{field[x+1]}|{field[x+2]}\n'
    return result

def checkWin(field : list):
    #по горизонтали
    for x in range(0, 9, 3):
        if field[x + 0] == field[x + 1] == field[x + 2] != ' ':
            return True
    #по вертикали
    for x in range(0, 3):
        if field[x + 0] == field[x + 3] == field[x + 6] != ' ':
            return True
    #по диагонали
    if field[0] == field[4] == field[8] != ' ':
        return True
    if field[2] == field[4] == field[6] != ' ':
        return True
    return False

def drawSelectCell(field : list, ind : int):
    if len(field) != 9:
        return ''
    if ind < 0 or ind >= 9:
        return ''
    new_field= list.copy(field)
    new_field[ind] = '*'
    return getStrField(new_field)

def getIndFirstFreeCeil(field : list):
    for x in range(0, len(field)):
        if field[x] == ' ':
            return x
    return -1

def updateConsole(player : bool, field : list, current_cell : int):
    if player:
        print('Ходит игрок 2') #'o'
    else:
        print('Ходит игрок 1') #'x'
    print(drawSelectCell(field, current_cell))

def getFreeCell(field : list):
    return [x for x in range(0, 9) if field[x] == ' ']

def moveSelection(field : list, current_cell : int, direction : Direction):
    freeCell = getFreeCell(field)
    tmpt_cell = 0
    if direction == Direction.left:
        return freeCell[freeCell.index(current_cell) - 1]
    elif direction == Direction.right:
        return freeCell[(freeCell.index(current_cell) + 1) % len(freeCell)]
    elif direction == Direction.up:
        if current_cell - 3 in freeCell:
            return current_cell - 3
        elif current_cell - 6 in freeCell:
            return current_cell - 6
        else:
            return current_cell
    elif direction == Direction.down:
        if current_cell + 3 in freeCell:
            return current_cell + 3
        elif current_cell + 6 in freeCell:
            return current_cell + 6
        else:
            return current_cell

field : list = [' '] * 9
player = False
lose = False

while True:
    current_cell = getIndFirstFreeCeil(field)
    if current_cell  == -1:
        lose = True
        break
    clear()
    updateConsole(player, field, current_cell)
    sleep(0.8)
    key = keyboard.read_key()
    while key != 'enter':
        if key == 'left':
            current_cell = moveSelection(field, current_cell, Direction.left)
        elif key == 'right':
            current_cell = moveSelection(field, current_cell, Direction.right)
        elif key == 'up':
            current_cell = moveSelection(field, current_cell, Direction.up)
        elif key == 'down':
            current_cell = moveSelection(field, current_cell, Direction.down)
        clear()
        updateConsole(player, field, current_cell)
        sleep(0.2)
        key = keyboard.read_key()
    if player:
        field[current_cell] = 'o'
    else:
        field[current_cell] = 'x'

    if checkWin(field):
        break
    else:
        player = not player

clear()
if lose:
    print('Ничья')
else:
    if player:
        print('Победил игрок 2!') #'o'
    else:
        print('Победил игрок 1!') #'x'
print(getStrField(field))
sleep(1)
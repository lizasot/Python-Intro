def getEncodeStr(text : str):
    result = ''
    current_char = text[0]
    count_repeat = 1
    for x in range(1,len(text)):
        if current_char != text[x]:
            result += str(count_repeat)
            result += current_char
            count_repeat = 1
            current_char = text[x]
        else:
            count_repeat += 1
    result += str(count_repeat)
    result += current_char
    return result

def encodeFile(filename_input : str, filename_output : str):
    with open(filename_input,'r') as f_in, open(filename_output,'w') as f_out:
        text = f_in.read()
        f_out.write(getEncodeStr(text))

def getDecodeStr(text : str):
    result = ''
    x = 0
    y = 0
    iter = 0
    while x != len(text):
        while text[y].isdigit():
            y += 1
        iter = int(text[x:y])
        result += text[y] * iter
        y += 1
        x = y
    return result

def decodeFile(filename_input : str, filename_output : str):
    with open(filename_input,'r') as f_in, open(filename_output,'w') as f_out:
        text = f_in.read()
        f_out.write(getDecodeStr(text))



print('[1] Сжать файл inputRLE.txt в outputRLE.txt')
print('[2] Восстановить файл inputUnRLE.txt в outputUnRLE.txt')
choice = int(input('Введите 1 или 2 для выбора: '))
if choice == 1:
    encodeFile('inputRLE.txt','outputRLE.txt')
    print('Файл успешно сжат в outputRLE.txt')
elif choice == 2:
    decodeFile('inputUnRLE.txt','outputUnRLE.txt')
    print('Файл успешно восстановлен в outputUnRLE.txt')
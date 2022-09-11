numb  = int(input('Введите число: '))

fib_list : list = []
nefib_list : list = []

for x in range(0,numb+1):
    if x == 0:
        fib_list.append(0)
    elif x == 1:
        fib_list.append(1)
        nefib_list.append(1)
    else:
        fib_list.append(fib_list[x-1]+fib_list[x-2])
        if x % 2 == 0:
            nefib_list.append(-(fib_list[x-1]+fib_list[x-2]))
        else:
            nefib_list.append((fib_list[x-1]+fib_list[x-2]))
nefib_list.reverse()
nefib_list += fib_list
print(nefib_list)
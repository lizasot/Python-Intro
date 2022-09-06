def has_number(l : list):
    for x in range(0,len(l)):
        for y in range(0,10):
            if str(y) in l[x]:
                print(f'Найдено число в строке под индексом {x}')
                break;

l : list = ['dfsfd','fdf5','dfsd3','3433fdsd','3','d']

has_number(l)
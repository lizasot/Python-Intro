def differenceFractional(l : list):
    if len(l) == 0:
        return
    min_fract = 0
    max_fract = 0
    for x in range(1,len(l)):
        if l[x] % 1 != 0:
            if l[x] != 0 and (min_fract > (l[x] % 1) or min_fract == 0):
                min_fract = l[x] % 1
            if l[x] != 0 and (max_fract < (l[x] % 1) or max_fract == 0):
                max_fract = l[x] % 1
    return round(max_fract - min_fract, 5)

print(f'[1.1, 1.2, 3.1, 5, 10.01] => {differenceFractional([1.1, 1.2, 3.1, 5, 10.01])}')
def has_second_str(l : list, s : str):
    met : bool = 0
    for x in range(0,len(l)):
        if s == l[x]:
            if met == 1:
                return x
            else:
                met = 1
    return -1

print(has_second_str(["qwe", "asd", "zxc", "qwe", "ertqwe"], 'qwe'))
print(has_second_str(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], 'йцу'))
print(has_second_str(["йцу", "фыв", "ячс", "цук", "йцукен"], 'йцу'))
print(has_second_str(["123", "234", 123, "567"], '123'))
print(has_second_str([], '123'))
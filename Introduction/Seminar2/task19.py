import datetime

def my_randint(beg : int, end : int):
    end += 1
    current_date = datetime.datetime.now()
    time = int(current_date.strftime("%Y%m%d%H%M%S"))
    return (time % (end - beg)) + beg

print('Случайное число от 0 до 1:')
print(my_randint(0,1))
print('Случайное число от 0 до 5:')
print(my_randint(0,5))
print('Случайное число от -8 до 5:')
print(my_randint(-8,5))
print('Случайное число от 25 до 95:')
print(my_randint(25,95))
from datetime import datetime

time = datetime.now()


def decorator(time):
    return time


@decorator
def fact(number):
    if number == 0:
        return 1
    return number * fact(number - 1)


number = int(input('введите число '))
print('Факториaл числа', number, ':', fact(number), 'время выполнения', time)

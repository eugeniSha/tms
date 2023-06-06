def search(number):
    if number >= 0:
        print(f"Вы ввели целое число: {number}")
    elif number <= 0:
        print(f"Вы ввели отрицательное целое число: {number}")
    elif float(number) >= 0:
        print(f"Вы ввели дробное число: {number}")
    elif float(number) <= 0:
        print(f"Вы ввели отрицательное дробное число: {number}")
    else:
        print(f"Вы ввели некоректное число: {number}")


number = input('Введите число ')
search(number)

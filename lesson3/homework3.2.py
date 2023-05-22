name = input('Bведите имя ')
age = input('Bаш возраст ').isdigit()
ages = int(age)
if ages:
    if ages <= 0:
        print('Ошибка, повторите ввод')
    elif ages < 10:
        print(f'Привет, шкет {name}')
    elif 10 <= ages <= 18:
        print(f'Как жизнь {name}?')
    elif 18 <= ages <= 100:
        print(f'Что желаете {name}?')
    elif ages < 100:
        print(f'{name},вы лжец-в наше время столько не живут...')
else:
    print(f'Ошибка, повторите ввод')

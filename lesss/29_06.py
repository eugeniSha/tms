import typing

"""
1. Объект-генератор реализуют интерфейс Итератора: в самом общем смысле, Генератор это и есть Итератор. 
Причем, чтобы написать свой Итератор, используя Генератор, не нужно описывать отдельный класс с методами 
__iter__ и __next__ 
"""


# my_gen - функция-генератор, так как содержит оператор yield
def my_gen(some_list):
    for i in some_list:
        yield i


my_list = [1, 2, 3, 4, 5]
my_iterator = my_gen(my_list)  # вызов функции-генератора НЕ выполняет код внутри функции - он лишь
# возвращает объект-генератор, который мы можем потом использовать

# в данном примере мы используем генератор как итератор для списка
for i in my_iterator:
    print(i)

# Код внутри функции-генератора начинает выполняться, когда к созданному ей
# объекту-генератору "обратятся" через вызов next()

"""
2. Генераторы - ленивые. Они отдают один элемент по очереди "по запросу" 
и не хранят все данные в памяти одновременно
"""
import sys

from_one_to_million_list = [i for i in range(1000001)]  # list comprehension возвращает список
print(sys.getsizeof(from_one_to_million_list))

from_one_to_million_gen = (i for i in range(1000001))
# а это - генераторное выражение: еще один способ создать объект-генератор из последовательности элементов
print(sys.getsizeof(from_one_to_million_gen))

# sys.getsizeof() возращает размер переданного его объекта в байтах.
# from_one_to_million_gen будет занимать гораздо меньше места в памяти, чем from_one_to_million_list
# так как список хранит все инты от 1 до миллиона в памяти (+ доп. память для новых элементов)

"""
3. Генераторы работают таким образом, что позволяют выполняющемуся внутри коду "засыпать", 
сохраняя при этом текущее состояние объекта, а после - "просыпаться" и продолжать выполнение
с того места, на котором генератор "заснул" 
"""


def generator_function(some_list: typing.List):
    func_name = generator_function.__qualname__

    print(f"'{func_name}': Generator started")

    for idx, elem in enumerate(some_list):
        print(f"'{func_name}': Returning name '{elem}' and then suspending...")
        yield elem
        print(f"'{func_name}': Awaking!")

        if idx < len(some_list) - 1:
            print(f"'{func_name}': Continue working...")
        else:
            print(f"'{func_name}': Exit")
    print("gen is end")


def iterate_over_names(names: typing.List):
    func_name = iterate_over_names.__qualname__
    print(f'{func_name}' ' when start')
    gen = generator_function(names)
    counter = 0
    for name in gen:
        counter+=1
        print(f'iterationN{counter}')
        print(f"'{func_name}': Current name is '{name}'")
    print(f'{func_name}' ' when finish')

iterate_over_names(
    ['Ann', 'Alex', 'John', 'Olga', 'Mary']
)
# iterate_over_names(['John', 'Olga', 'Mary'])


#
# import requests
#
#
# resp = requests.get ("http://google.com")
# print(resp)
#
"""regex101.com"""
import re
regex_email_patten = r'[a-zA-Z\d]+@[a-z]+.[a-z]{2,3}'
regex_email_patten = re.compile(regex_email_patten)
user_email = 'user@gmail.com'
print(re.sub(r'[a-s]','0', user_email))


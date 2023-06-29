import typing
import random
"""
ИТЕРИРУЕМЫЕ ОБЪЕКТЫ (Iterable)
"""

class ListWrapper:
    """
    Данный класс:
    - создает внутри себя список из полученных на этапе инициализации аргументов
    - позволяет итерироваться по экземпляру, реализуя метод __iter__
    """
    def __init__(self, *args):
        self._list = args

    def __str__(self):
        return f"MyList object: {self._list}"

    def __iter__(self):
        """
        Метод __iter__ возващает ссылку на Объект-Итератор, класс которого реализован ниже
        """
        return ListWrapperIterator(self._list)


"""
ИТЕРАТОРЫ (Iterators)
"""

class ListWrapperIterator:
    """
    Данный класс реализует интерфейс Итератора (пригоден только для работы со списками)
    """

    def __init__(self, some_list):
        self._some_list = some_list  # неизменнно с момента инициализации
        self._size = len(self._some_list)  # неизменнно с момента инициализации
        self._curr_index = 0  # увеличивается на 1 при каждом вызове __next__!

    def __iter__(self):
        """
        Для совместимости объектов-итераторов с iterable-объектами,
        класс итератора должен реализовывать метод __iter__, который
        лишь возвращает ссылку на свой же экземпляр
        """
        return self

    def __next__(self):
        """
        Метод __next__ объекта-итератора реализует логику получения следующего элемента из последовательности
        В данном случае, атрибут экземпляра '_curr_index' хранит текущее значение индекса и увеличивается на 1
        при каждом вызове метода __next__, пока не будет достигнут лимит
        """
        if self._curr_index < self._size:
            # 1. Получить элемент из внутреннего списка по индексу 'self._curr_index'
            result = self._some_list[self._curr_index]
            # 2. Увеличить значение 'self._curr_index' на 1
            self._curr_index += 1
            # 3. Вернуть полученный элемент
            return result
        else:
            # необходимо выбросить StopIteration исключение, если значение 'self_curr_index'
            # достигло значеня 'self._size' value - это значит, что внутренний список "закончился"
            # и дальнейшие вызовы __next__ попросту не имеют смысла
            raise StopIteration



leeee =[]
limit = 10
while True:
    if limit >= 0:
        limit -= 1
        leeee.append(random.randint(0,100))
    else:
        break
my_list = ListWrapper(leeee)
print(my_list)

"""
Так как my_list это ссылка на экземпляр класса ListWrapper, который реализует 
метод __iter__ - значит экземпляр класса ListWrapper является Iterable-объектом
и по нему можно итерироваться с помощью цикла for
"""
for element in my_list:
    # Цикл for не знает точное количество раз, сколько раз ему нужно повторяться -
    # он повторяется до тех пор, пока не встретит StopIteration - обработает это исключение
    # и завершится без ошибок
    print(element)

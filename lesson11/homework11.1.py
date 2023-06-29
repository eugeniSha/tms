"""OOP (parts 2-3) Homework"""

from dataclasses import dataclass

"""
Домашнее Задание:

1. Описать Dataclass, который
- содержит три произвольных поля, разных типов
- имеет один-единственный classmethod, который:
  - проверяет типы этих трех полей и возвращает объект Dataclass'a, если типы верны 
  - порождает исключение TypeError если хотя бы один из атрибутов имеет НЕВЕРНЫЙ тип
- является НЕИЗМЕНЯЕМЫМ (у инстанса этого класса нельзя изменить значения атрибута/добавить новый атрибут/удалить атрибут)
"""


# TASK 1: Шаблон класса
@dataclass
class MyDataClass:
    a: str
    b: int
    c: list

    @classmethod
    def build(cls, a, b, c):
        if isinstance(a, str) and isinstance(b, int) and isinstance(c, list):
            print("valid parameters")



# Тесты для задания 1: должны отработать без ошибок!
person1 = MyDataClass.build("TEST", 34, [1, 2, 3])  # valid parameters
print(person1)
try:
    person2 = MyDataClass.build(100, 33, [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", "33", [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", 33, (1, 2, 3))  # invalid parameters
except Exception as exc:
    print(exc)

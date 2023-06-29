import random


# **********************************************************************************************************************


# leeee = []
# limited = 10
# while True:
#     if limited >= 0:
#         limited -= 1
#         leeee.append(random.randint(0, 100))
#     else:
#         break
#
#
# class RandomValue:
#     def __init__(self, limit):
#         self.limit = limit
#         self._list = leeee
#
#
#     def __iter__(self):
#
#         return RandomValueIterator(self.limit)
#
#
#
# class RandomValueIterator:
#     def __init__(self, leeee):
#         self._some_list = leeee
#         self._size = 20
#         self._curr_index = 0
#
#     def __iter__(self):
#
#         return self
#
#     def __next__(self):
#
#         if self._curr_index < self._size:
#             result = self._some_list[self._curr_index]
#             self._curr_index += 1
#             return result
#         else:
#            raise StopIteration
#
#
#
# my_limit = int(input("Введите лимит: "))
# my_random = RandomValue(limit=my_limit)
#
# results = [elem for elem in my_random]
# print(results)
#
# assert len(results) == my_limit
# for i in results:
#     assert i is not None


# **********************************************************************************************************************


# class RandomValue:
#     def __init__(self, limit):
#         self.limit = limit
#         self.list = []
#
#     def __iter__(self):
#         return RandomValueIterator
#
#     def rand(self):
#         if not self.limit == 0:
#             self.list_.append(random.randint(0, 101))
#             self.limit -= 1
#         else:
#             return self.list_
#
#
# class RandomValueIterator:
#     def __init__(self):
#         self._curr_index = my_random.self.limit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._curr_index > 0:
#             self._curr_index -+ 1
#         else:
#             raise StopIteration
#
#
# my_limit = int(input("Введите лимит: "))
# my_random = RandomValue(limit=my_limit)
#
# results = [elem for elem in my_random]
# print(results)
#
# assert len(results) == my_limit
# for i in results:
#     assert i is not None


# **********************************************************************************************************************


class RandomValue:
    def __init__(self, limit):
        self.limit = limit
        self.list = []

    def __iter__(self):
        return RandomValueIterator

    def rand(self):
        while True:
            if self.limit >= 0:
                self.limit -= 1
                self.list.append(random.randint(0, 100))
            break


class RandomValueIterator:
    def __init__(self, limit):
        self.curr_index = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index > 0:
            self.curr_index -+ 1
        else:
            raise StopIteration


my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None

# **********************************************************************************************************************

# class RandomValue:
#     def __init__(self):
#         self._list = list()
#
#     def __iter__(self):
#         return RandomValueIterator ()
#
#
# class RandomValueIterator:
#     def __init__(self):
#
#
#     def __iter__(self):
#
#
#
#     def __next__(self):
#     """Your implementation here"""
#
#
# my_limit = int(input("Введите лимит: "))
# my_random = RandomValue(limit=my_limit)
#
# results = [elem for elem in my_random]
# print(results)
#
# assert len(results) == my_limit
# for i in results:
#     assert i is not None

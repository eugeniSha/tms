import random


class RandomValue:
    def __init__(self, limit):
        self.limit = limit
        self.curr_index = 0

    def __iter__(self):
        while self.curr_index < self.limit:
            self.curr_index += 1
            yield random.randint(0, 100)



# class RandomValueIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.curr_index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.curr_index < self.limit:
#             self.curr_index += 1
#             return random.randint(0, 100)
#         else:
#             raise StopIteration

my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None

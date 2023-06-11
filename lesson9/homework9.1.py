import time


class auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = int(age)
        self.mark = mark
        self.color = 'color'
        self.weight = 'weight'

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        print(self.age)


class truck(auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)

    def move(self):
        print('attention')
        super().move()


class car(auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed is <{self.max_speed}>')


""" test car"""
# test = car('audi', '2', 's6', '222')
# test.stop()
# test.birthday()
# test.move()
# test_1 = car('tesla', '21', 'model S', '303')
# test_1.stop()
# test_1.birthday()
# test_1.move()


""" test truck"""
# test_truck = truck('audi', '2', 's6', '2500')
# test_truck.move()
# test_truck.load()
# test_truck.birthday()
# test_truck.stop()
# truck_test = truck('CAT', '6', 'w3', '2020')
# truck_test.move()
# truck_test.load()
# truck_test.birthday()
# truck_test.stop()

from datetime import datetime, time
from time import sleep


import time

def real_time():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

n = int(input("Введите количество элементов в списке: "))
time_list = [real_time() for i in range(n)]
print(time_list)

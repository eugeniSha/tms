my_list = list(range(1, 101))
result = [x for x in my_list if x % 10 == 0] + \
        [c*10 for c in my_list if c % 4 != 0] + \
        [r*2 for r in my_list if r % 4 == 0]

print(result)
words = ('довод', 'пример', 'доход')
a = []

for i in words:
    if i == i[::-1]:
        a.append(i)

print(a)

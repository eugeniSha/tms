from collections import Counter
numbers = [1, 2, 3, 4, 2, 3, 1, 1, 5, 6, 7, 5, 4, 3]
counts = Counter(numbers)
for number, count in counts.items():
    print(f'Число {number} встречается {count} раз')
# n = int( input('введите целое число '))
# start = 0
# summ = 0
# while start < n:
#     qube = (start+1)**3
#     summ = summ + qube
#     start = start+1
# print (summ)

n = int(input('введите целое число '))
start: int = 0
summ = 0
for int in range(0,n):
    qube = (start + 1) ** 3
    summ = summ + qube
    start = start + 1
print(summ)

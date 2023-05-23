

number = input('введите число ')
number = int(number)
answer = 0
while not answer == number:
    if number == 0:
        print('ваше число ', answer)

    elif number >= 0:
        answer += 1
    else:
        answer -= 1
print('ваше число ', answer)


def not3(num):
    if num == 1 or num == 2:
        return False
    if num == 3:
        return True
    else:
        return not3(num-3)


def not5(num):
    if num == 1 or num == 2 or num == 3 or num == 4:
        return False
    if num == 5:
        return True
    else:
        return not5(num-5)


num=20
three=not3(num)

five=not5(num)

print(three,five)



def get_hcf(number1, number2):
    if number1 > number2:
        small = number2
    else:
        small = number1

    for n in range(1, small + 1):
        if ((number1 % n == 0) and (number2 % n == 0)):
            hcf = n
    return hcf


def get_lcm(number1, number2):
    if number1 > number2:
        greater = number1
    else:
        greater = number2

    while (True):
        if ((greater % number1 == 0) and (greater % number2 == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


if __name__ == '__main__':
    print(get_hcf(5, 12))
    print(get_lcm(5, 12))


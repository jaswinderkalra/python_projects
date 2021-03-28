def is_prime(number):
    if number > 1:
        for n in range(2, int(number ** 0.5) + 1):
            if number % n == 0:
                return 'The number is not prime'
    return 'The number is prime'


def is_valid(number):
    if number > 1:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(-10, 100):
        if is_valid(i):
            print(str(i) + " " + is_prime(i))
        else:
            print(str(i) + " " + 'The number is invalid')

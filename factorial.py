def get_factorial(number):
    p = 1
    for i in range(number, 1, -1):
        p = p * i
    return p

if __name__ == '__main__':
    for i in range(0, 6):
        print(get_factorial(i))

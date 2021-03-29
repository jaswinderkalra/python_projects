class Factorise:

    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2

    def get_hcf(self):
        big, small = self.get_big_small()
        for n in range(1, small + 1):
            if (self.number1 % n == 0) and (self.number2 % n == 0):
                hcf = n
        return hcf

    def get_lcm(self):
        big, small = self.get_big_small()
        while True:
            if (big % self.number1 == 0) and (big % self.number2 == 0):
                lcm = big
                break
            big += 1
        return lcm

    def get_big_small(self):
        return max(self.number1, self.number2), min(self.number1, self.number2)


if __name__ == '__main__':
    f = Factorise(9, 12)
    print("lcm: ",f.get_lcm(), " hcf: ", f.get_hcf())

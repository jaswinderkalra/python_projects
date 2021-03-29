class Factorise:

    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2

    def get_hcf(self):
        if self.number1 > self.number2:
            small = self.number2
        else:
            small = self.number1

        for n in range(1, small + 1):
            if ((self.number1 % n == 0) and (self.number2 % n == 0)):
                hcf = n
        return hcf

    def get_lcm(self):
        if self.number1 > self.number2:
            greater = self.number1
        else:
            greater = self.number2

        while (True):
            if ((greater % self.number1 == 0) and (greater % self.number2 == 0)):
                lcm = greater
                break
            greater += 1
        return lcm


if __name__ == '__main__':
    # print(get_hcf(5, 12))
    # print(get_lcm(5, 12))
    f = Factorise(9,12)
    print(f.get_lcm()," ",f.get_hcf())

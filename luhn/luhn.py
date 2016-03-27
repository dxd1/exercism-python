class Luhn:
    def __init__(self, number):
        self.create(number)

    def create(self, number):
        self.number = number

    def addends(self):
        numbers = []
        parity = False
        for c in str(self.number)[::-1]:
            if parity:
                numbers.append(int(c)*2 if int(c)*2 < 10 else int(c)*2-9)
            else:
                numbers.append(int(c))
            parity = not(parity)
        print numbers[::-1]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum%10 == 0

import random

class Robot:

    def __init__(self):
        self.reset()

    def reset(self):
        random.seed()
        self.name =  self.letter()+self.letter()+self.number()+self.number()+self.number()

    def letter(self):
        return chr(random.randint(65,90))

    def number(self):
        return str(random.randint(0,9))

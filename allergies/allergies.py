class Allergies:
    allergies = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats'
    ]
    lst = []

    def __init__(self, score):
        self.lst = list(allergy for allergy, number in zip(self.allergies, format(score, '08b')[::-1]) if number == '1')

    def is_allergic_to(self, what):
        return what in self.lst

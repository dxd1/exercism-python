from collections import defaultdict

class School:

    def __init__(self, name):
        self.name = name
        self.db =  defaultdict(lambda: set())

    def add(self, name, grade):
        self.db[grade].add(name)

    def grade(self, grade):
        return self.db[grade]

    def sort(self):
        for grade in self.db:
            yield (grade, tuple(sorted(self.db[grade])))

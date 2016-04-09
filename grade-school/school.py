from collections import defaultdict

class School:

    def __init__(self, name):
        self.name = name
        self.db =  defaultdict(set)

    def add(self, name, grade):
        self.db[grade].add(name)

    def grade(self, grade):
        return self.db[grade]

    def sort(self):
        return ((grade, tuple(sorted(value))) for (grade, value) in self.db.items())

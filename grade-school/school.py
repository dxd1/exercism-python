class School:

    def __init__(self, name):
        self.name = name
        self.db = {}

    def add(self, name, grade):
        if not grade in self.db:
            self.db[grade] = set()
        self.db[grade].add(name)

    def grade(self, grade):
        if not grade in self.db:
            return set()
        else:
            return self.db[grade]

    def sort(self):
        for grade in self.db:
            grade_list = list(self.db[grade])
            grade_list.sort()
            yield (grade, tuple(grade_list))

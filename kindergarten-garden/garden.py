class Garden:
    plant_dictionary = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, garden, students = None):
        self.garden = []
        if students is None:
            self.children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.children = sorted(students)
        line1, line2 = garden.split("\n")
        self.garden = list(zip(line1[::2], line1[1::2], line2[::2], line2[1::2]))

    def plants(self, child):
        return [self.plant_dictionary[i] for i in self.garden[self.children.index(child)]]

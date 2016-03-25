class Garden:
    plant_dictionary = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, garden, students = []):
        self.garden = []
        if students == []:
            self.children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            students.sort()
            self.children = students
        lines = garden.split("\n")
        for i in range(0, len(lines[0]), 2):
            self.garden.insert(int(i/2), [])
        for line in lines:
            for i in range(0, len(line), 2):
                self.garden[int(i/2)].append(self.plant_dictionary[line[i]])
                self.garden[int(i/2)].append(self.plant_dictionary[line[i+1]])



    def plants(self, child):
        return self.garden[self.children.index(child)]

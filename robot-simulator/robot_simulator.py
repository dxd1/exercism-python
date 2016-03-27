NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing+=1
        if self.bearing == 4:
            self.bearing = 0

    def turn_left(self):
        self.bearing-=1
        if self.bearing == -1:
            self.bearing = 3

    def advance(self):
        coordinates = list(self.coordinates)
        if(self.bearing == NORTH):
            coordinates[1] += 1
        elif(self.bearing == EAST):
            coordinates[0] += 1
        elif(self.bearing == SOUTH):
            coordinates[1] -= 1
        elif(self.bearing == WEST):
            coordinates[0] -= 1
        self.coordinates = tuple(coordinates)

    def simulate(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'A':
                self.advance()

from wall import Wall

class Maze:
    def __init__(self):
        self.walls = []

    def add_wall(self, wall):
        self.walls.append([wall.position, wall.size])

    def spawn(self):
        print("parede existe")



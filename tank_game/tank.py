
class Tank:
    def __init__(self, name, lifes, position):
        self.name = name
        self.lifes = lifes
        self.position = position

    def move_r(self):
        self.position += 5
        print(self.name, self.position)

    def get_hit(self):
        self.lifes -= 1
        print("DANOOOOOOOOOOOOOOO")


class Tank2:
    def __init__(self, name, lifes, position):
        self.name = name
        self.lifes = lifes
        self.position = position

    def move_f(self, name):
        self.position -= 5
        print(self.name, self.position)

    def get_hit(self):
        self.lifes -= 1
        print("DANOOOOOOOOOOOOOOO")




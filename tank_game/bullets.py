class Bullets:
    def __init__(self, position):
        self.position = position

    def movement(self):
        self.position += 5
        print(self.position)

    def collide(self):
        print("Bullet collide")

    def shot(self, tank):
        self.position += tank.position
        print("Atirei")

class Bullets:

    def __init__(self, shooter, target):
        self.pos_x = shooter.pos_x
        self.pos_y = shooter.pos_y
        self.shooter = shooter
        self.target = target
        print(f"Bullet atirada por {self.shooter.name}")

    def movement(self):
        self.pos_x += 5
        self.pos_y += 5
        print(f"bala na posição x:{self.pos_x} e posição y:{self.pos_y}")

    def collide(self):
        print("Bullet collide")
        self.target.alive = False

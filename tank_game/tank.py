from bullets import Bullets
import time


class Tank:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_r(self):
        self.pos_x += 5
        self.pos_y += 5
        print(f"{self.name} se move para a posição X: {self.pos_x}, y:{self.pos_y}")
        time.sleep(0.3)

    def shoot(self, target):
        if self.alive:
            bullet = Bullets(self, target)
            for i in range (11):
                bullet.movement()
                time.sleep(0.4)

        else:
            print(f"Tank :{self.name} não pode atirar porque está destruído.")

    def get_hit(self):
        self.alive = False
        print(f"{self.name} foi derrotado")



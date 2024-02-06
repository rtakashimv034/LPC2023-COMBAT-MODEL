from wall import Wall

class Maze:
    def __init__(self):
        self.walls = []
        print(f"{'-'*10}[INICIO DO JOGO]{'-'*10}")
        print("Status: Maze foi Criado")

    def add_wall(self, wall):
        self.walls.append(wall)





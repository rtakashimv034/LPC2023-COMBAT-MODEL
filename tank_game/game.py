from tank import Tank
from maze import Maze
from wall import Wall


class Game:
    def __init__(self):
        self.game_start = True

    def game_running(self):
        if self.game_start:
            maze = Maze()
            maze.add_wall(Wall(size=(1, 1), position=(0, 0)))
            t_1 = Tank("Player 1", 0, 0)
            t_2 = Tank("Player 2", 50, 50)
            t_1.move_r()
            t_1.move_r()
            t_1.move_r()
            t_1.move_r()
            t_2.move_r()
            t_1.move_r()
            t_2.move_r()
            t_2.move_r()
            t_2.move_r()
            t_1.shoot(t_2)
            t_2.get_hit()
            self.game_start = False
        else:
            print(f"{'-'*10}[JOGO ENCERRADO]{'-'*10}")



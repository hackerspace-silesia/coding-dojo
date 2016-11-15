from logic import BaseGame

class Player(object):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    DIRECTIONS = set([LEFT, RIGHT, UP, DOWN])

    def __init__(self):
        self.position = [0, 0]
        self.movement_direction = None

    def get_position(self):
        return self.position

    def set_direction(self, direction):
        if direction not in self.DIRECTIONS:
            raise ValueError('wrong direction')
        self.movement_direction = direction

    def move(self):
        if self.movement_direction == self.LEFT:
            self.position[0] -= 1
        elif self.movement_direction == self.RIGHT:
            self.position[0] += 1
        elif self.movement_direction == self.UP:
            self.position[1] -= 1
        elif self.movement_direction == self.DOWN:
            self.position[1] += 1


class Pacman(Player):

    def __init__(self):
        self.position = (15, 15)
        self.movement_direction = None
        self.live = 3

    def get_life_points(self):
        return self.live


class PacmanMap(object):
    MAX_X = 20
    MAX_Y = 32

    WALL = 0
    CANDY = 1

    def __init__(self):
        self.storage = [
            [None for x in range(self.MAX_X)] 
            for y in range(self.MAX_Y)]

    def add_object(self, x, y, obj):
        if ( x >= 0 and x < self.MAX_X and
            y >= 0 and y < self.MAX_Y ):
            self.storage[y][x] = obj
        else:
            raise IndexError

    def get_object(self, x, y):
        return self.storage[y][x]

    def lets_build_a_wall(self):
        for x in range(self.MAX_X):
            self.add_object(x, 0, 0)
        for y in range(self.MAX_Y):
            self.add_object(0, y, 0)




    # def _get_line(self, y):
    #     try:
    #         line = self.storage[y]
    #     except IndexError:
    #         line = []
    #         self.storage[y] = line
    #     return line

class Game(BaseGame):

    def init(self):
        self.pmap = PacmanMap()
        self.pacman = Pacman()

    def loop(self, key):
        if key == 'w':
            pass # Todo

        # x, y koordynacja w planszy
        # x od 0 do 20
        # y od 0 do 32
        # self.draw_pacman(x, y) 
        # self.draw_wall(x, y)
        # self.draw_point(x, y)
        # self.draw_ghost(x, y)
        # self.draw_text(x, y, 'string')
        self.draw_pacman(0, 0)
        self.draw_wall(1, 1)  # ▓
        self.draw_ghost(2, 2) # ☢
        self.draw_point(3, 3) # +
        self.draw_point(4, 4) # +
        self.draw_text(33, 0, 'SIEMA')


if __name__ == "__main__":
    from curses import wrapper
    wrapper(Game().base_loop)

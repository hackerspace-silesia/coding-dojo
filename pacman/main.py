from logic import BaseGame


class Game(BaseGame):
    t = 0

    def init(self):
        pass

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
        self.t = 1 - self.t
        self.draw_pacman(0, 0)
        self.draw_wall(1, 1)  # ▓
        self.draw_ghost(2, 2) # ☢
        self.draw_point(3, 3) # +
        self.draw_point(4, 4) # +
        self.draw_text(33, 0, 'SIEMA')


if __name__ == "__main__":
    from curses import wrapper
    wrapper(Game().base_loop)

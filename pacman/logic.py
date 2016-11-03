import curses
from random import randint
PACMAN = '☻'
WALL = '▓'
POINT = '+'
GHOST = '☢'

YELLOW = 12
BLUE = 5
WHITE = 16
RED = 10

LEFT, RIGHT, UP, DOWN = '<>^v'


class BaseGame(object):
    stdscr = None

    def draw(self, x, y, s, color):
        assert x in range(0, 32)
        assert y in range(0, 20)
        self.stdscr.addstr(y + 1, x + 1, s, curses.color_pair(color))

    def draw_pacman(self, x, y, direction=PACMAN):
        self.draw(x, y, direction, YELLOW)

    def draw_wall(self, x, y):
        self.draw(x, y, WALL, BLUE)

    def draw_point(self, x, y):
        self.draw(x, y, POINT, WHITE)

    def draw_ghost(self, x, y):
        self.draw(x, y, GHOST, RED)

    def draw_text(self, x, y, s):
        self.stdscr.addstr(y + 1, x + 1, s, curses.color_pair(WHITE))

    def base_loop(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        curses.start_color()
        curses.use_default_colors()
        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)
        stdscr.keypad(1)
        stdscr.timeout(300)
        self.init()

        key = None
        while key != 'q':
            stdscr.clear()
            try:
                stdscr.vline(0, 0, '#', 21, curses.color_pair(WHITE))
                stdscr.vline(0, 33, '#', 21, curses.color_pair(WHITE))
                stdscr.hline(0, 0, '#', 33, curses.color_pair(WHITE))
                stdscr.hline(21, 0, '#', 33, curses.color_pair(WHITE))
                self.loop(key)
            except curses.error:
                pass
            stdscr.refresh()
            try:
                key = stdscr.getkey()
            except curses.error:
                key = None


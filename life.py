# this is a python script
# that shows interaction of
# particles using curses module

# importing libraries
import curses
import random


class life:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # initialising the window
    def winInit(self):
        self.win = curses.newwin(self.width, self.height, 0, 0)
        self.win.clear()
        self.win.border()
        self.win.keypad(True)

    # creating one particle
    def oneParticle(self, positions, colorNumber):
        # for coloring the particles we
        # are initialising the curses color
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        self.win.addch(positions[0], positions[1],
                       curses.ACS_BULLET, curses.color_pair(colorNumber))

    # creating many particle
    def manyParticles(self, particles, colorNumber):
        while (particles != 0):
            self.oneParticle(positions=(random.randint(1, 28),
                                        random.randint(1, 88)),
                             colorNumber=colorNumber)
            particles -= 1

    # the main loop
    def winRun(self):
        self.manyParticles(150, colorNumber=1)
        self.manyParticles(150, colorNumber=2)
        self.manyParticles(150, colorNumber=3)
        self.manyParticles(150, colorNumber=4)

        while True:
            self.key = self.win.getch()
            if self.key == ord("q"):
                break

        self.win.refresh()


# the main function
def main(stdscr):
    particleLife = life(30, 90)
    particleLife.winInit()
    particleLife.winRun()


if __name__ == "__main__":
    curses.wrapper(main)

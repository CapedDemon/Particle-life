# this is a python script
# that shows interaction of
# particles using curses module

# importing libraries
import curses
from math import sqrt
import random


class life:
    def __init__(self, height, width):
        self.width = width
        self.height = height

    # initialising the window
    def winInit(self):
        self.win = curses.newwin(self.height, self.width, 0, 0)
        self.win.clear()
        self.win.border()
        self.win.keypad(True)

    # creating one particle
    def oneParticle(self, x, y, colorNumber):
        # for coloring the particles we
        # are initialising the curses color
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        # printing particle with a specific color code.
        self.win.addch(y, x,
                       curses.ACS_BULLET, curses.color_pair(colorNumber))

    # return x, y, color, velocity-x, velocity-y
    def returnParticle(self, x, y, color, vx, vy):
        return {"x":x, "y":y, "color":color, "vx":vx, "vy":vy}


    # creating many particle
    def manyParticles(self, particles, colorNumber):
        group = []
        while (particles != 0):
            x = random.randint(1, 88)
            y = random.randint(1, 28)
            vx = 0
            vy = 0
            # self.oneParticle(x, y,
            #                  colorNumber=colorNumber)
            group.append(self.returnParticle(x, y, colorNumber, vx, vy))
            particles -= 1

        return group
    

    def drawParticles(self, particles):
        i = len(particles) - 1
        while i >= 0:
            self.oneParticle(particles[i]["x"],
                             particles[i]["y"], particles[i]["color"])
            i -= 1


    # force of attraction
    # F = GmM/R^2
    def mainRule(self, particles1, particles2, g):
        fx =0 
        fy =0

        a = particles1[0]
        b = particles2[1]
        rx = b["x"]-a["x"]
        ry = b["y"]-a["y"]
        r = int(sqrt(pow(rx, 2)+pow(ry, 2)))
        print(r)
        if (r > 0):
            F = int(g*1/r)
            fx += (F*rx)
            fy += (F*ry)
            self.blue[0]["x"] += fx
            self.blue[0]["y"] += fy


            #print(a["x"])

    # the main loop
    def winRun(self):
        self.win.timeout(100)
        self.blue = self.manyParticles(2, colorNumber=1)
        # self.manyParticles(150, colorNumber=2)
        # self.manyParticles(150, colorNumber=3)
        # self.manyParticles(150, colorNumber=4)
        fx = 0
        fy = 0
        while True:
            print(self.blue[0]["x"])
            self.drawParticles(self.blue)
            self.blue[0]["x"] += 1
            self.blue.pop()
            print("x", self.blue[0]["x"])
            self.key = self.win.getch()
            if self.key == ord("q"):
                break
            
            # print(self.blue[0]["x"], self.blue[1]["y"])

        self.win.refresh()


# the main function
def main(stdscr):
    stdscr.clear()
    particleLife = life(30, 90)
    particleLife.winInit()
    particleLife.winRun()


if __name__ == "__main__":
    curses.wrapper(main)

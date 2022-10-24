# importing the required libraries
import pygame
from pygame.locals import *
import random
import math

class Particle:
    def __init__(self, running, width, height, color):
        # initialising pygame
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Particle Life")  # setting title
        self.screen.fill(color)

        pygame.display.update()
        self.running = running

        # initialising clock
        self.clock = pygame.time.Clock()

        # colors
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.yellow = (255, 255, 0)

    # function to create
    # one particle on the scree

    def createParticle(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x, y, 2, 2))

    # returns a dict

    def returnParticle(self, x, y, color, vx, vy):
        return {"x": x, "y": y, "color": color, "vx": vx, "vy": vy}

    # returns a list consisting
    # of all the necessary things

    def manyParticles(self, number, color):
        group = []
        for i in range(number):
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            vx = 0
            vy = 0

            group.append(self.returnParticle(x, y, color, vx, vy))
        return group

    # the function to create
    # many particles

    def createParticles(self, particles):
        for particle in particles:
            self.createParticle(
                particle["x"], particle["y"], particle["color"])

    # this is the mainrule function
    # which follows F = GMm/r^2
    # and this will move the particles towards each other
    # and also coordinate geometry = squareroot[(x2-x1)^2 + (y2-y1)^2]
    # and also F = ma

    def mainRule(self, particles1, particles2, g):
        # first iterating over all the particles in the particles1
        for i in range(len(particles1)):
            # setting the force to be applied
            # in the x and y coordinates
            fx = 0
            fy = 0

            # now iterating over the particles2
            for j in range(len(particles2)):
                a = particles1[i]
                b = particles2[j]
                dx = a["x"]-b["x"]
                dy = a["y"]-b["y"]
                # using coordinate geometry to find the distance between two particles
                d = math.sqrt(dx*dx+dy*dy)
                if (d > 0):
                    F = g*1/d
                    fx += (F*dx)
                    fy += (F*dy)

            a["vx"] = (a["vx"] + fx)*0.5
            a["vy"] = (a["vy"] + fy)*0.5
            # due to the forc applied
            # the particles also face acceleration
            # so setting the velocity using the force formula
            a["x"] += a["vx"]
            a["y"] += a["vy"]

            # now reversing the particles
            # when they hit the wall
            if (a["x"] <= 0 or a["x"] >= 700):
                a["vx"] *= -1
            elif (a["y"] <= 0 or a["y"] >= 500):
                a["vy"] *= -1
        self.screen.fill(0)

    # the main loop

    def gameLoop(self):
        # defining particles
        self.yellowParticles = self.manyParticles(200, self.yellow)
        self.redParticles = self.manyParticles(200, self.red)
        self.greenParticles = self.manyParticles(200, self.green)
        self.blueParticles = self.manyParticles(200, self.blue)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # creating the particles
            self.createParticles(self.yellowParticles)
            self.createParticles(self.redParticles)
            self.createParticles(self.greenParticles)
            self.createParticles(self.blueParticles)

            # updating the display
            pygame.display.update()

            # enter your rules here
            # defining the rules
            self.mainRule(self.yellowParticles, self.yellowParticles, -0.1)

            self.clock.tick(78)
        pygame.quit()

# the main function


def main():
    particleLife = Particle(True, 700, 500, (0, 0, 0))
    particleLife.gameLoop()


if __name__ == "__main__":
    main()

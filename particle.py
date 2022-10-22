# importing the required libraries
import pygame
from pygame.locals import *
import random
import math

from regex import D


class particle:
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

        # colors
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)

    # function to create
    # one particle on the scree

    def createParticle(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x, y, 2, 2))
        pygame.display.update()

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

    def mainRule(self, particles1, particles2, g):
        fx = 0
        fy = 0
        a = particles1[0]
        b = particles2[1]
        dx = a["x"]+b["x"]
        dy = a["y"]+b["y"]
        d = math.sqrt(dx*dx+dy*dy)
        if (d>0):
            F= g*1/d
            fx += (F*dx)
            fy += (F*dy)
        a["x"] +=fx
        a["y"] +=fy


    # the main loop
    def gameLoop(self):
        self.blueParticles = self.manyParticles(2, self.blue)
        print(self.blueParticles)
        while self.running:
            print(self.blueParticles[0]["x"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.createParticles(self.blueParticles)
            self.mainRule(self.blueParticles, self.blueParticles, 1)
        pygame.quit()

# the main function


def main():
    particleLife = particle(True, 700, 500, (0, 0, 0))
    particleLife.gameLoop()


if __name__ == "__main__":
    main()

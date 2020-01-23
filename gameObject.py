import constants
import pygame

class GameObject():
    def __init__(self, location, image):
        self.location = location
        self.image = image
        self.alive = True

    def isAlive(self):
        return self.alive

    def getLocation(self):
        return self.location

    def updateLocation(self, location):
        self.location = location

    def update(self, direction, speed):
        self.location.update(direction, speed)

    def draw(self, display):
        surface = pygame.image.load(self.image)

        display.blit(
            surface,
            self.location.listify()
        )
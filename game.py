import pygame
from player import Player
from food import Food
from location import Location
import constants

class Game():
    def __init__(self):
        self.player = Player()
        self.food = Food()
        self.points = 0
        self.ticks = 0
        self.running = False
        self.foodExists = False

    def startGame(self):
        pygame.init()
        clock = pygame.time.Clock()
        display = pygame.display.set_mode((500,500))
        self.running = True

        while self.running:
            clock.tick(15)
            self.ticks += 1
            self.eventController()
            self.collisionController()
            self.inputController()
            self.foodController()
            self.updateController()
            self.drawController(display)

    def eventController(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

    def inputController(self):
        keyInput = pygame.key.get_pressed()

        if keyInput[pygame.K_ESCAPE]:
            self.running = False
            return

        if keyInput[pygame.K_UP] and self.player.head.direction != constants.downDir:
            self.player.head.updateDirection(constants.upDir)
        if keyInput[pygame.K_DOWN] and self.player.head.direction != constants.upDir:
            self.player.head.updateDirection(constants.downDir)
        if keyInput[pygame.K_LEFT] and self.player.head.direction != constants.rightDir:
            self.player.head.updateDirection(constants.leftDir)
        if keyInput[pygame.K_RIGHT] and self.player.head.direction != constants.leftDir:
            self.player.head.updateDirection(constants.rightDir)

    def drawController(self, display):
        display.fill((0, 0, 0))

        self.food.draw(display)

        for tail in self.player.body:
            tail.draw(display)

        pygame.display.flip()

    def updateController(self):
        for tail in self.player.body:
            tail.update()
                

    def collisionController(self):
        if self.player.head.getLocation() == self.food.getLocation():
            self.points += 1
            self.player.addTail()
            self.foodExists = False

    def foodController(self):
        if self.foodExists == False:
            self.food.updateLocation(Location(self.food.getRandomLocation(), self.food.getRandomLocation()))
            self.foodExists = True
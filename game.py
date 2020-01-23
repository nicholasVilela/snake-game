import pygame
from player import Player
from food import Food
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
            self.inputController()
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

        if keyInput[pygame.K_UP] and self.player.direction != constants.downDir:
            self.player.updateDirection(constants.upDir)
        if keyInput[pygame.K_DOWN] and self.player.direction != constants.upDir:
            self.player.updateDirection(constants.downDir)
        if keyInput[pygame.K_LEFT] and self.player.direction != constants.rightDir:
            self.player.updateDirection(constants.leftDir)
        if keyInput[pygame.K_RIGHT] and self.player.direction != constants.leftDir:
            self.player.updateDirection(constants.rightDir)

    def drawController(self, display):
        display.fill((0, 0, 0))

        for gameObject in [self.player]:
            gameObject.draw(display)

        pygame.display.flip();

    def updateController(self):
        self.player.update()

    def foodController(self):
        pass
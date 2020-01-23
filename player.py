from gameObject import GameObject
from location import Location
import constants

class Player(GameObject):
    def __init__(self):
        GameObject.__init__(
            self,
            Location(250, 250),
            './images/snake-image.png'
        )

        self.direction = constants.upDir
        self.speed = 10
        self.tail = []

    def update(self):
        GameObject.update(self, self.direction, self.speed)

    def updateDirection(self, direction):
        self.direction = direction
from gameObject import GameObject
import constants as const

class Cube(GameObject):
    def __init__(self, speed, location, image, direction=const.rightDir):
        self.direction = direction
        self.speed = speed
        GameObject.__init__(
            self,
            location,
            image
        )

    def update(self):
        GameObject.update(self, self.direction, self.speed)

    def updateTailLocation(self, direction, speed):
        GameObject.update(self, direction, speed)

    def updateDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
from gameObject import GameObject

class Cube(GameObject):
    def __init__(self, direction, speed, location, image):
        self.direction = direction
        self.speed = speed
        GameObject.__init__(
            self,
            location,
            image
        )

    def update(self):
        GameObject.update(self, self.direction, self.speed)

    def updateDirection(self, direction):
        self.direction = direction

    def getDirection(self):
        return self.direction
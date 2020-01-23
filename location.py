import constants

class Location():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def listify(self):
        return [self.x, self.y]

    def update(self, direction, speed):
        if direction == constants.downDir:
            self.y += speed
        elif direction == constants.upDir:
            self.y -= speed
        elif direction == constants.leftDir:
            self.x -= speed
        elif direction == constants.rightDir:
            self.x += speed
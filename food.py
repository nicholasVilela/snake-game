from gameObject import GameObject
from location import Location
import random
import constants

class Food(GameObject):
    def __init__(self):
        GameObject.__init__(
            self,
            Location(self.getRandomLocation(), self.getRandomLocation()),
            './images/food-image.png'
        )

    def getRandomLocation(self):
        return random.randrange(0, 500, 10)
        
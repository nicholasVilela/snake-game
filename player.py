from gameObject import GameObject
from location import Location
from tail import Tail
from cube import Cube
import constants as const

class Player():
    def __init__(self):
        self.head = Cube(
            const.upDir,
            10,
            Location(250, 250),
            './images/snake-image.png'
        )
        self.body = []
        self.body.append(self.head)

    def getTailLength(self):
        return len(self.body)

    def addTail(self):
        tail = self.body[-1]
        dx = tail.getLocationX()
        dy = tail.getLocationY()
        d = tail.getDirection()

        if d == const.downDir:
            newTail = Cube(
                d,
                10,
                Location(
                    tail.getLocationX(),
                    tail.getLocationY() - 10
                ),
                './images/snake-image.png'
            )
        if d == const.upDir:
            newTail = Cube(
                d,
                10,
                Location(
                    tail.getLocationX(),
                    tail.getLocationY() + 10
                ),
                './images/snake-image.png'
            )

        if d == const.leftDir:
            newTail = Cube(
                d,
                10,
                Location(
                    tail.getLocationX() + 10,
                    tail.getLocationY()
                ),
                './images/snake-image.png'
            )

        if d == const.rightDir:
            newTail = Cube(
                d,
                10,
                Location(
                    tail.getLocationX() - 10,
                    tail.getLocationY()
                ),
                './images/snake-image.png'
            )
        
        self.body.append(newTail)

        # self.body[-1].location.x = dx
        # self.body[-1].location.y = dy
        self.body[-1].direction = d
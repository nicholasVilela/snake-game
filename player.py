from gameObject import GameObject
from location import Location
from tail import Tail
from cube import Cube
from node import Node
import pygame
import constants as const

class Player():
    body = []

    def __init__(self):
        self.head = Node(Cube(
            10,
            Location(250, 250),
            './images/snake-image.png',
            const.upDir
        ))

        self.body.append(self.head)

    def getTailLength(self):
        return len(self.body)

    def addTail(self):
        tail = self.body[-1]
        print(tail)
        d = tail.cube.getDirection()

        if d == const.downDir:
            newTail = Node(
                Cube(
                    10,
                    Location(
                        tail.cube.getLocationX(),
                        tail.cube.getLocationY() - 10
                    ),
                    './images/snake-image.png'
                ),
                tail
            )
        if d == const.upDir:
            newTail = Node(Cube(
                10,
                Location(
                    tail.cube.getLocationX(),
                    tail.cube.getLocationY() + 10
                ),
                './images/snake-image.png'
            ), tail)

        if d == const.leftDir:
            newTail = Node(Cube(
                10,
                Location(
                    tail.cube.getLocationX() + 10,
                    tail.cube.getLocationY()
                ),
                './images/snake-image.png'
            ), tail)

        if d == const.rightDir:
            newTail = Node(Cube(
                10,
                Location(
                    tail.cube.getLocationX() - 10,
                    tail.cube.getLocationY()
                ),
                './images/snake-image.png'
            ), tail)
        
        self.body.append(newTail)
        self.body[-1].cube.updateDirection(self.body[-1].forward.cube.getDirection())

    def updateTailLocation(self):
        self.body[-1].cube.updateDirection(self.body[-1].forward.cube.getDirection())
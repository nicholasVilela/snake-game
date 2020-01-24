from cube import Cube

class Node():
    def __init__(self, cube, forward=None):
        self.cube = cube
        self.direction = self.cube.getDirection()
        self.location = self.cube.getLocation()
        self.forward = forward
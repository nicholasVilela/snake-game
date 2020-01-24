from gameObject import GameObject

class Tail(GameObject):
    def __init__(self, location, image):
        GameObject.__init__(
            self,
            location,
            image
        )

    def update(self, direction, speed):
        GameObject.update(self, direction, speed)
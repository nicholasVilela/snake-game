from gameObject import GameObject

class Tail(GameObject):
    def __init__(self, location, image):
        GameObject.__init__(
            self,
            location,
            image
        )
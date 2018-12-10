class Entity():

    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        # Implement animation (Array of images? Dealt with by qt?)
        self.image = None

    def is_touching(self, Entity):
        if (self.x <= Entity.x + Entity.width and self.x + self.width <= Entity.x and
        self.y <= self.x + Entity.height and self.y + self.height <= Entity.y):
            return True
        return False

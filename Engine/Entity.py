import math

class Entity():
    """General code for things that appear in the world."""

    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        # Implement animation (Array of images? Dealt with by qt?)
        self.image = None

    def isTouching(self, entity):
        """Checks if an entity is in contact with another"""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if (self.x <= entity.x + entity.width and
            self.x + self.width <= entity.x and
            self.y <= self.x + entity.height and
            self.y + self.height <= entity.y):
            return True
        return False

    def isInRange(self, entity, range):
        """Checks the bounds of the given entity against its own."""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if math.sqrt(((self.x + self.width / 2) - (entity.x + entity.width / 2))**2 +
                     ((self.y + self.height / 2) - (entity.y + entity.height / 2))**2) <= range:
            return True
        return False

    def getImage(self, scale):
        """Returns the image associated with the entity."""
        if self.image == None:
            return None

        return self.image.scaled(int(100*scale), int(100*scale))

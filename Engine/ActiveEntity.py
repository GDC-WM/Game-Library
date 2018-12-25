import math

from Entity import Entity

class ActiveEntity(Entity):
    """A type of entity that allows for movement within the world."""

    def __init__(self):
        super().__init__()
        self.physical = False
        self.mass = 0
        self.x_speed = 0
        self.y_speed = 0
    
    def physics(self):
        """Applies the appropriate affects of game physics to the entity"""
        if self.physical:
            pass

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def run(self):
        """User implementation of run method."""
        pass
    
    def push(self, vector):
        """Adds a momentum vector to the entity\n
        vector -- magnitude and direction (radians) in a tuple
        """
        self.x_speed = (self.mass*self.x_speed+vector[0]*math.cos(vector[1]))/self.mass
        self.y_speed = (self.mass*self.y_speed+vector[0]*math.sin(vector[1]))/self.mass

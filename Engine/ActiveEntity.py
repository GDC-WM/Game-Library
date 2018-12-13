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
        """Applies a force vector to the entity\n
        vector -- magnitude and direction of the force
        """

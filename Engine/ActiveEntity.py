from Entity import Entity

class ActiveEntity(Entity):

    def __init__(self):
        super().__init__()
        self.mass = 0;

    def physics(self):
        pass

    def run(self):
        pass

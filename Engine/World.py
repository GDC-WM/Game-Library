class World():

    def __init__(self):
        self.__entity_list = []

        # View offset for the camera to facilitate scrolling
        # These are added to the x and y value of each entity when rendered
        self.__view_x = 0
        self.__view_y = 0

    def draw_screen(self, qp):
        # TODO: fill this in with code to draw all the objects onscreen
        pass

    def addEntity(self, entity, x, y):
        entity.x = x
        entity.y = y
        self.__entity_list.append(entity)

    def removeEntity(self, entity):
        self.__entity_list.remove(entity)

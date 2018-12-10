class World():

    def __init__(self):
        self.__entity_list = []

    def addEntity(self, entity):
        self.__entity_list.append(entity)

    def removeEntity(self, entity):
        self.__entity_list.remove(entity)

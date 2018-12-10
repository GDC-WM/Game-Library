from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class World():

    def __init__(self, engine):
        self.__entity_list = []

        self.engine = engine
        self.background = None  # This should be a QImage

        # View offset for the camera to facilitate scrolling
        # These are added to the x and y value of each entity when rendered
        self.__view_x = 0
        self.__view_y = 0

        self.__screen_width = engine.size().width()
        self.__screen_height = engine.size().height()

    def draw_screen(self, qp):
        for e in self.__entity_list:
            if e.image != None:
                if (e.x + e.width/2 + self.__view_x < 0 and 
                    e.x - e.width/2 + self.__view_x > self.__screen_width and
                    e.y + e.height/2 + self.__view_y < 0 and
                    e.y - e.height/2 + self.__view_y > self.__screen_height):

                    qp.drawImage(QPoint(e.x, e.y), e.image)


    def addEntity(self, entity, x, y):
        entity.x = x
        entity.y = y
        self.__entity_list.append(entity)

    def removeEntity(self, entity):
        self.__entity_list.remove(entity)

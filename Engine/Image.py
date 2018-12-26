import sys
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import Qt, QRect, QPoint

class Image():

    def __init__(self, image):

        self.__image = QImage(image) 

    def setScale(self, xFactor, yFactor):
        self.__image = self.__image.scaled(self.getWidth()*xFactor, self.getHeight()*yFactor)

    def getScale(self, factor):
        return self.__image.scaled(self.getWidth()*factor, self.getHeight()*factor)

    def getWidth(self):
        return self.__image.size().width()

    def getHeight(self):
        return self.__image.size().height()

import sys
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import Qt, QRect, QPoint

class Image():

    def __init__(self, image):

        self.image = QImage(image) 

    def width():
        return self.image.size().width()

    def height():
        return self.image.size().height()

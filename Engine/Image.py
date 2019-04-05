import sys
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import Qt, QRect, QPoint

class Image():
    
    def __init__(self, filename):
        self.image = QImage(filename)
        self.scale = 1
        self.width = self.getWidth()
        self.height = self.getHeight()

    def getImage(self):
        return self.image.scaled(self.getWidth()*self.scale,
                                 self.getHeight()*self.scale)

    def setScale(self, factor):
        self.scale = factor

    def setSize(self, xSize, ySize):
        self.image = self.image.scaledToWidth(xSize)
        self.image = self.image.scaledToHeight(ySize)

    def getScaled(self, factor):
        return self.getImage().scaled(self.getWidth()*self.scale*factor, 
                                      self.getHeight()*self.scale*factor)

    def getWidth(self):
        return self.image.size().width()

    def getHeight(self):
        return self.image.size().height()

class ImageGroup():

    def __init__(self):
        self.images = []
        self.image_index = 0

    def addImage(self, image):
        self.images.append(image)
    
    def getImage(self):
        return self.images[self.image_index]

    def setStart(self):
        self.image = self.images[0]

    def nextImage(self):
        self.image_index = (self.image_index + 1) % len(self.images)

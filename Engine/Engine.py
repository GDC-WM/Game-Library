from World import World

import sys, time
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class Engine(QWidget):
    def __init__(self):
        super().__init__()

        self.__active_world = World(self)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.drawImage(QPoint(0,0), self.__active_world.background)
        self.__active_world.draw_screen(qp)
        
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()
    sys.exit(app.exec_())

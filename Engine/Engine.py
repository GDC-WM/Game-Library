import sys, time
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class Engine(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()
    sys.exit(app.exec_())

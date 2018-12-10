from World import World

import sys, time, threading
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class Engine(QWidget):
    def __init__(self):
        super().__init__()

        self.__active_world = World(self)
        self.__running = True

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.drawImage(QPoint(0,0), self.__active_world.background)
        self.__active_world.draw_screen(qp)
        
        qp.end()

    def run(self):
        while self.__running:
            start_time = time.time()
            
            # Do stuff here
            
            if (time.time() - start_time < 1/60):
                time.sleep(1/60 - (time.time() - start_time))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()

    t1 = threading.Thread(target=ex.run())
    t1.start()

    sys.exit(app.exec_())

from World import World

import sys, time
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QScreen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QThread, QObject

class Engine(QWidget):

    class RunThread(QThread):
        def __init__(self, engine):
            QtCore.QThread.__init__(self) 
            self.engine = engine
            self.running = True
        
        def run(self):
            while self.running:
                self.engine.active_world.run()
                time.sleep(.1)

    def __init__(self):
        super().__init__()

        self.setFixedSize(QScreen.size(QApplication.primaryScreen()).width(), 
                          QScreen.size(QApplication.primaryScreen()).height())
        #set scale based on relation to 1080p
        self.scale = QScreen.size(QApplication.primaryScreen()).width()/1080
        self.showFullScreen()

        self.active_world = World(self)
        
        self.run_thread = self.RunThread(self)
        self.run_thread.start()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.drawImage(QPoint(0,0), self.active_world.background)
        self.active_world.draw_screen(qp)
        
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()
    sys.exit(app.exec_())

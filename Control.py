from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, QStatusBar, QPushButton
import sys
import KeyboardControl as kc

class UI(QMainWindow):
   def __init__(self):
      super(UI, self).__init__()
      uic.loadUi('Control.ui', self)

      self.Qland = self.findChild(QPushButton, "Qland")
      self.Etakeoff = self.findChild(QPushButton, "Etakeoff")
      self.Wup = self.findChild(QPushButton, "Wup")
      self.Sdown = self.findChild(QPushButton, "Sdown")
      self.Drotate_r = self.findChild(QPushButton, "Drotate_r")
      self.Arotate_l = self.findChild(QPushButton, "Arotate_l")

      self.forward = self.findChild(QPushButton, "forward")
      self.back = self.findChild(QPushButton, "back")
      self.right = self.findChild(QPushButton, "right")
      self.left = self.findChild(QPushButton, "left")

      self.Qland.clicked.connect(self.land)
      self.Etakeoff.clicked.connect(self.takeoff)


      self.show()

   def takeoff(self):
       kc.me.takeoff()

   def land(self):
       kc.me.land()



app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()
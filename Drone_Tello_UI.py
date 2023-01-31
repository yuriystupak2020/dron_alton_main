from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QLabel, QSlider, QTextEdit, QProgressBar, QStatusBar
import sys

class UI(QMainWindow):
   def __init__(self):
      super(UI, self).__init__()
      uic.loadUi('Drone_Tello_UI.ui', self)

      self.textBat = self.findChild(QPlainTextEdit, "textBat")
      self.textWiFi = self.findChild(QPlainTextEdit, "textWiFi")
      self.textWiFi = self.findChild(QPlainTextEdit, "textWiFi")

      self.progressBarBat = self.findChild(QProgressBar, "progressBarBat")
      self.progressBarWiFi = self.findChild(QProgressBar, "progressBarWiFi")
      self.progressBarWiFi = self.findChild(QProgressBar, "progressBarWiFi")

      self.labelReply = self.findChild(QLabel, "Order")
      self.labelOrder = self.findChild(QLabel, "Order")


      self.show()


app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()
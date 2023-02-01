import sys
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5


#python -m pip install --upgrade --force-reinstall PyQt5
# python3 configure.py --qmake [path to Qt5.x]/bin/qmake для импорта всех модулей

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        print('Key pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())

from PyQtGUI import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtGui import QPixmap, QImage
import sys


from PyQt5.QtCore import QTimer , QRunnable, QThreadPool
import datetime
from PyQt5.QtWidgets import (QTableWidgetItem,QActionGroup, QApplication, QFileDialog,
		QGraphicsItem, QGraphicsRectItem, QGraphicsScene, QGraphicsView,
		QMainWindow, QMenu, QMessageBox, QWidget)




class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.StartWebCam)
        self.ui.pushButton_2.clicked.connect(self.StopWebCam)
        self.timer=QTimer()
        self.timer.timeout.connect(self.UpdateFrame)


    def StartWebCam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer.start(5)

    def UpdateFrame(self):
        ret, self.img = self.capture.read()
        self.img=cv2.flip(self.img,1)
        self.displayImage(self.img,1)

    def StopWebCam(self,img,window=1):
        self.timer.stop()
        self.capture.release()

    def displayImage(self,img,window=1):
        qformat=QImage.Format_Indexed8

        if len(img.shape)==3:
            if img.shape[2]==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img,img.shape[1], img.shape[0],img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.ui.label.setPixmap(QPixmap.fromImage(outImage))
            self.ui.label.setScaledContents(True)



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    # myapp.Exit()
    sys.exit(app.exec_())








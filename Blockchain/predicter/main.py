import os,sys
import datetime as dt

try:
    import colorama
except:
    os.system("python -m pip install colorama")
    import colorama
try:
    import pandas as pd
except:
    os.system("python -m pip install pandas")
    import pandas as pd

try:
    import pickle
except:
    os.system("python -m pip install pickle-mixin")
    import pickle
try:
    import numpy as np
except:
    os.system("python -m pip install numpy")
    import numpy as np

try:
    import sklearn
except:
    os.system("python -m pip install sklearn")
    import sklearn

try:
    import pickle
except:
    os.system("python -m pip install pickle-mixin")
    import pickle

try:
    import matplotlib.pyplot as plt
except:
    os.system('python -m pip install matplotlib')
    import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
from PIL import Image



#Constants
MODEL_NAME="ourmodel.sav"


class Predicter:
    def __init__(self):
        self.model = pickle.load(open(MODEL_NAME,"rb"))

    def formatDate(self,date:tuple):
        if len(date) != 3:
            raise ValueError("Date should be composed from 3 elements YYYY MM DD")
        date = (str(date[0]),str(f"0{date[1]}" if date [1] < 10 else f"{date[1]}"),str(f"0{date[2]}" if date [2] < 10 else f"{date[2]}"))#Ensure format YYYY-MM-DD
        date = dt.datetime.fromisoformat("{}-{}-{}".format(*date))
        return date
    def predict(self,dateA:tuple,dateB:tuple):
        dateA = self.formatDate(dateA)
        dateB = self.formatDate(dateB)
        dates = pd.to_datetime(np.array([dateA,dateB]))
        dates = dates.map(dt.datetime.toordinal)
        #Range berechnen
        dates = np.array([i for i in range(dates[0],dates[1] + 1)],dtype="int64")
        dates = np.reshape(dates,(-1,1))
        preds = self.model.predict(dates)
        return dates,preds

model = Predicter()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 220, 221, 41))
        self.pushButton.setObjectName("Predict Range")
        self.pushButton.clicked.connect(self.clicked)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 274, 781, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.pictureLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pictureLayout.setContentsMargins(0, 0, 0, 0)
        self.pictureLayout.setObjectName("pictureLayout")
        self.labelKurv = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelKurv.setText("")
        self.labelKurv.setObjectName("labelKurv")
        self.pictureLayout.addWidget(self.labelKurv)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.event
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget_2.setGeometry(QtCore.QRect(470, 20, 312, 183))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 60, 101, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.logoLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.logoLayout.setContentsMargins(0, 0, 0, 0)
        self.logoLayout.setObjectName("logoLayout")
        self.logoLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.logoLabel.setStyleSheet("background-image: url(bitcoin.png);background-size:cover;")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.logoLayout.addWidget(self.logoLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
    def calendar_changed(self):
        print("dsds")

    def clicked(self):
        dateRange1 = self.calendarWidget.selectedDate().getDate()
        dateRange2 = self.calendarWidget_2.selectedDate().getDate()
        dates,pred = model.predict(dateRange1,dateRange2)
        label_width,label_height = self.labelKurv.size().width(),self.labelKurv.size().height()
        plt.plot(dates,pred.reshape(-1,1))
        plt.savefig("kurv.png")
        image = Image.open("kurv.png")
        image = image.resize((label_width, label_height), Image.ANTIALIAS)
        image.save(fp="kurv.png")
        self.labelKurv.setStyleSheet("background-image: url(kurv.png);background-repeat: no-repeat;")

def launch():
    app = QtWidgets.QApplication(sys.argv)
    windows = QtWidgets.QMainWindow()
    diabete = Ui_MainWindow()
    diabete.setupUi(windows)
    diabete.retranslateUi(windows)
    windows.show()
    sys.exit(app.exec_())







launch()
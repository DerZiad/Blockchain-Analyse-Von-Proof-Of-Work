import time,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPainter,QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QListView,QGraphicsScene
import threading

from globalconfig.HardwareScanner import *


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 843)
        MainWindow.setStyleSheet(
            "backgorund-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.centralLayout.setContentsMargins(25, 25, 25, 25)
        self.centralLayout.setSpacing(20)
        self.centralLayout.setObjectName("centralLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(50, 15, 50, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicCardLayout = QtWidgets.QHBoxLayout()
        self.graphicCardLayout.setContentsMargins(10, 10, 10, 10)
        self.graphicCardLayout.setSpacing(25)
        self.graphicCardLayout.setObjectName("graphicCardLayout")
        self.gpuView = QtWidgets.QGraphicsView(self.centralwidget)

        self.gpuView.setObjectName("gpuView")
        self.gpuView.setMinimumSize(QtCore.QSize(400, 200))
        self.gpuView.setMaximumSize(QtCore.QSize(700, 200))
        self.graphicCardLayout.addWidget(self.gpuView)

        self.gpuList = QtWidgets.QListView(self.centralwidget)
        self.gpuList.setObjectName("gpuList")
        self.gpuList.setSelectionMode(QListView.SingleSelection)
        self.graphicCardLayout.addWidget(self.gpuList)
        self.graphicCardLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.graphicCardLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changeToGPULayout = QtWidgets.QHBoxLayout()
        self.changeToGPULayout.setObjectName("changeToGPULayout")
        self.gpuCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gpuCheckbox.setFont(font)
        self.gpuCheckbox.setObjectName("gpuCheckbox")
        self.changeToGPULayout.addWidget(self.gpuCheckbox)
        self.verticalLayout.addLayout(self.changeToGPULayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.cpuCard = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpuCard.sizePolicy().hasHeightForWidth())
        self.cpuCard.setSizePolicy(sizePolicy)
        self.cpuCard.setMinimumSize(QtCore.QSize(400, 200))
        self.cpuCard.setMaximumSize(QtCore.QSize(700, 200))
        self.cpuCard.setObjectName("cpuCard")
        self.horizontalLayout.addWidget(self.cpuCard)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.centralLayout.addLayout(self.verticalLayout_2)
        self.formularLayout = QtWidgets.QFormLayout()
        self.formularLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.formularLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formularLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formularLayout.setLabelAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.formularLayout.setFormAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignTop)
        self.formularLayout.setContentsMargins(25, 25, 25, 25)
        self.formularLayout.setHorizontalSpacing(250)
        self.formularLayout.setVerticalSpacing(20)
        self.formularLayout.setObjectName("formularLayout")
        self.nonceLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nonceLabel.sizePolicy().hasHeightForWidth())
        self.nonceLabel.setSizePolicy(sizePolicy)
        self.nonceLabel.setMinimumSize(QtCore.QSize(400, 40))
        self.nonceLabel.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nonceLabel.setFont(font)
        self.nonceLabel.setObjectName("nonceLabel")
        self.formularLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nonceLabel)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.formularLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.difficultyLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.difficultyLabel.sizePolicy().hasHeightForWidth())
        self.difficultyLabel.setSizePolicy(sizePolicy)
        self.difficultyLabel.setMinimumSize(QtCore.QSize(400, 40))
        self.difficultyLabel.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.difficultyLabel.setFont(font)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.formularLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.difficultyLabel)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(300, 40))
        self.textEdit_2.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formularLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.blockInformtionsTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockInformtionsTextEdit.sizePolicy().hasHeightForWidth())
        self.blockInformtionsTextEdit.setSizePolicy(sizePolicy)
        self.blockInformtionsTextEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.blockInformtionsTextEdit.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.blockInformtionsTextEdit.setFont(font)
        self.blockInformtionsTextEdit.setObjectName("blockInformtionsTextEdit")
        self.formularLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.blockInformtionsTextEdit)
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setMinimumSize(QtCore.QSize(120, 40))
        self.browseButton.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browseButton.setFont(font)
        self.browseButton.setObjectName("browseButton")
        self.formularLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.browseButton)
        self.mineButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mineButton.sizePolicy().hasHeightForWidth())
        self.mineButton.setSizePolicy(sizePolicy)
        self.mineButton.setMinimumSize(QtCore.QSize(120, 40))
        self.mineButton.setMaximumSize(QtCore.QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mineButton.setFont(font)
        self.mineButton.setObjectName("mineButton")
        self.formularLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mineButton)
        self.actionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionLabel.sizePolicy().hasHeightForWidth())
        self.actionLabel.setSizePolicy(sizePolicy)
        self.actionLabel.setMinimumSize(QtCore.QSize(400, 40))
        self.actionLabel.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.actionLabel.setFont(font)
        self.actionLabel.setObjectName("actionLabel")
        self.formularLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.actionLabel)
        self.centralLayout.addLayout(self.formularLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.timestampLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.timestampLabel.setFont(font)
        self.timestampLabel.setObjectName("timestampLabel")
        self.verticalLayout_3.addWidget(self.timestampLabel)
        self.centralLayout.addLayout(self.verticalLayout_3)
        self.console = QtWidgets.QListView(self.centralwidget)
        self.console.setStyleSheet("background-color:black;\n"
                                   "color:green;")
        self.console.setObjectName("console")
        self.centralLayout.addWidget(self.console)
        self.centralLayout.setStretch(0, 1)
        self.centralLayout.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.running = True
        self.waitingTime = 2

        gpuUpdater = threading.Thread(target=self.updateGPUStat)
        gpuUpdater.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IWantBTC"))
        self.gpuCheckbox.setText(_translate("MainWindow", "GPU Benutzen"))
        self.nonceLabel.setText(_translate("MainWindow", "Nonce"))
        self.difficultyLabel.setText(_translate("MainWindow", "Difficulty"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.mineButton.setText(_translate("MainWindow", "Mine"))
        self.actionLabel.setText(_translate("MainWindow", "Action"))
        self.timestampLabel.setText(_translate("MainWindow", "Timestamp"))

    def updateGPUListView(self,listOfGPUS):
        gpuCardNames = []
        for gpuCard in listOfGPUS:
            gpuCardNames.append(gpuCard.gpu_name)
        self.gpuListNames = gpuCardNames

        #Update graphic
        model = QStandardItemModel()

        # Append the items to the model
        for item in gpuCardNames:
            model.appendRow(QStandardItem(item))

        self.gpuList.setModel(model)
        self.gpuList.show()


        return gpuCardNames

    def updateGPUStat(self):
        while True:
            gpustatList:list = scanGPU()

            if len(gpustatList) != 0:
                # Check if the gpu stat is already loaded
                if not hasattr(self,"gpuListNames"):
                    self.gpuListNames = self.updateGPUListView(gpustatList)
                else:
                    if len(gpustatList) != len(self.gpuListNames):
                        self.gpuListNames = self.updateGPUListView(gpustatList)

                indexes = self.gpuList.selectedIndexes()
                if len(indexes) != 0:
                    index = indexes[0]
                    gpuStatistik:GPUStat = gpustatList[index.row()]


                    # Create a pie series and add some data slices to it
                    series = QPieSeries()
                    series.append("Slice 1", 20)
                    series.append("Slice 2", 25)
                    series.append("Slice 3", 30)

                    # Create a chart and add the pie series to it
                    chart = QChart()
                    chart.addSeries(series)
                    chart.setTitle("Simple pie chart example")

                    print("Before quitting")
                    scene = QGraphicsScene()
                    scene.addItem(chart)

                    self.gpuView.setScene(scene)
                    self.gpuView.setRenderHint(QPainter.Antialiasing)
                    self.gpuView.show()
            else:
                self.graphicCardLayout = None
            time.sleep(0.9)

    def updateCPUStat(self):
        pass

def launch():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

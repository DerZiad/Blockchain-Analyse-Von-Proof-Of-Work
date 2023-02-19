
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtGui import QPainter,QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QListView,QGraphicsScene
from PyQt5.QtCore import Qt
import random
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene

app = QApplication([])
# Create a series for the pie chart
series = QPieSeries()

# Add some slices to the pie chart
series = QPieSeries()
series.append("Slice 1", 20)
series.append("Slice 2", 25)
series.append("Slice 3", 30)

# Create a chart and add the pie series to it
chart = QChart()
chart.addSeries(series)
chart.setTitle("Simple pie chart example")

# Create a scene
scene = QGraphicsScene()

# Add the chart to the scene
scene.addItem(chart)

# Create a view to display the scene
view = QGraphicsView(scene)

# Set the render hints
view.setRenderHint(QPainter.Antialiasing, True)
view.setRenderHint(QPainter.SmoothPixmapTransform, True)

# Set the size of the view and show it
view.resize(400, 300)

view.show()

app.exec_()


import matplotlib.pyplot as plt
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize( 900,700)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.canvas)
        self.layout().setContentsMargins(0,0,0,0)
    

    def plot_data(self, x, y):
        self.ax.clear()

        # Plot the custom data with specified color
        self.ax.plot(x, y, color="#4167e1")

        # Set the color of the x-axis and y-axis
        self.ax.spines['bottom'].set_color("#4167e1")   # x-axis
        self.ax.spines['left'].set_color("#4167e1")    # y-axis
        self.ax.spines['top'].set_color("#ffffff")    # y-axis
        self.ax.spines['right'].set_color("#ffffff")    # y-axis
        

        # Set the color of the tick labels on the x-axis and y-axis
        self.ax.tick_params(axis='x', colors="#4167e1")
        self.ax.tick_params(axis='y', colors="#4167e1")

        self.canvas.draw()

class Graph_Screen_UI(object):
    def setupUi(self,graph_screen):

        graph_screen.setWindowTitle("PyQt5 Graph Example")
        graph_screen.resize(1000, 700)

        self.matplotlib_widget = MatplotlibWidget(graph_screen)

        self.x = [5,10,15,20]
        self.y = [9,4,2,7]

        layout = QVBoxLayout(graph_screen)
        layout.addWidget(self.matplotlib_widget)
        layout.setContentsMargins(0,0,0,0)
        self.plot_data()

       

    def plot_data(self):
        self.matplotlib_widget.plot_data(self.x, self.y)
        


    

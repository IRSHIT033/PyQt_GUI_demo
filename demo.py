from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.stackedWidget = QtWidgets.QStackedWidget()
        self.addWidget()

        self.label = QtWidgets.QLabel()
        self.label.setText("This is the label")

        self.stackedWidget.addWidget(self.label)

        self.show()

    def addWidget(self):
        self.widget = QtWidgets.QWidget()

        self.label = QtWidgets.QLabel()
        self.label.setText("This is the label")

        self.array = [1, 2, 3, 4, 5]

        for i in range(len(self.array)):
            self.label.setText(str(self.array[i]))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)

        self.widget.setLayout(self.layout)

        self.stackedWidget.addWidget(self.widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()

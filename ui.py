# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\analog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 411)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 621, 391))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page)

        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(310, 120, 55, 71))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(120, 220, 401, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("start")
        self.pushButton_4.clicked.connect(self.start_timer)
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("stop")
        self.pushButton_3.clicked.connect(self.stop_timer)
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(650, 10, 160, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 18))
        self.pushButton_2.setObjectName("redirect_logs_page")
        self.pushButton_2.clicked.connect(self.goto_logs_page)

        self.vboxlayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("redirect_graph_page")
        self.pushButton.clicked.connect(self.goto_graph_page)
        self.vboxlayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.current_number = 0

        self.capture_timer = QTimer()
        self.capture_timer.timeout.connect(self.capture_label_text)
        self.current_number = 0

        self.data_log = []
        self.capture_text_timer()

        layout = QtWidgets.QVBoxLayout(self.page)

        for number in self.data_log:
            label = QtWidgets.QLabel(str(number), self)
            layout.addWidget(label)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start_timer(self):
        self.timer.start(200)  # Update label every second

    def stop_timer(self):
        self.timer.stop()
        self.data_log.append(self.current_number)

    def capture_text_timer(self):
        self.capture_timer.start(5000)
        print('Captured data log', self.data_log)

    def update_label(self):
        self.current_number += 1
        if self.current_number > 20:
            self.current_number = 1
        self.label.setText(str(self.current_number))

    def capture_label_text(self):
        self.data_log.append(self.current_number)
        print('Captured data log', self.data_log)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "start"))
        self.pushButton_3.setText(_translate("MainWindow", "stop"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Log"))
        self.pushButton.setText(_translate("MainWindow", "Graph"))

    def goto_logs_page(self):
        self.timer.stop()
        self.capture_timerself.stop()
        self.stackedWidget.setCurrentIndex(0)

    def goto_home_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def goto_graph_page(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

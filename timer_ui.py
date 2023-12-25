from PyQt5 import QtCore, QtGui, QtWidgets
import pygame


class Timer_UI(object):
    def setupUi(self, timer_widget):
        timer_widget.setObjectName("timer_widget")

        pygame.mixer.init()

        self.apgar_timer = {
            1: False,
            3: False,
            5: False,
            10: False
        }

        self.timer = QtCore.QTimer(timer_widget)
        self.time_elapsed = 0
        self.timer.timeout.connect(self.updateTime)

        self.widget_11 = QtWidgets.QWidget(timer_widget)
        self.widget_11.setGeometry(QtCore.QRect(50, 60, 324, 117))
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_20 = QtWidgets.QWidget(self.widget_11)
        self.widget_20.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.widget_20.setFont(font)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#4169E1")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(
            self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.widget_20)
        self.widget_21 = QtWidgets.QWidget(self.widget_11)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.widget_21.setFont(font)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.timer_text = QtWidgets.QLabel(self.widget_21)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.timer_text.setFont(font)
        self.timer_text.setStyleSheet("color:#4169E1")
        self.timer_text.setObjectName("timer_text")
        self.horizontalLayout_10.addWidget(self.timer_text)
        self.start_stop_btn = QtWidgets.QPushButton(self.widget_21)
        self.start_stop_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.start_stop_btn.setFont(font)
        self.start_stop_btn.setStyleSheet("background:#4169E1;\n"
                                          "color:#ffffff;")
        self.start_stop_btn.setObjectName("start_stop_btn")
        self.horizontalLayout_10.addWidget(self.start_stop_btn)
        self.reset_btn = QtWidgets.QPushButton(self.widget_21)
        self.reset_btn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setStyleSheet("background:#4169E1;\n"
                                     "color:#ffffff;")
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout_10.addWidget(self.reset_btn)
        self.verticalLayout_10.addWidget(self.widget_21)

        self.retranslateUi(timer_widget)
        QtCore.QMetaObject.connectSlotsByName(timer_widget)

        self.start_stop_btn.clicked.connect(self.startStopwatch)
        self.reset_btn.clicked.connect(self.resetStopwatch)

    def retranslateUi(self, timer_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label_12.setText(_translate("Form", "Apgar Timer"))
        self.timer_text.setText(_translate("Form", "00:00"))
        self.start_stop_btn.setText(_translate("Form", "start"))
        self.reset_btn.setText(_translate("Form", "reset"))

    def startStopwatch(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            self.start_stop_btn.setText('Stop')
        else:
            self.timer.stop()
            self.start_stop_btn.setText('Start')

    def resetStopwatch(self):
        self.time_elapsed = 0
        self.apgar_timer = {key: False for key in self.apgar_timer}
        self.start_stop_btn.setText('Start')
        self.timer.stop()
        self.timer_text.setText('00:00')

    def bell_ring(self):
        pygame.mixer.music.load("./alarm.mp3")
        pygame.mixer.music.play()

    def updateTime(self):
        self.time_elapsed += 1
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        time_str = '{:02d}:{:02d}'.format(minutes, seconds)
        self.timer_text.setText(time_str)
        if self.timer.isActive() and seconds in self.apgar_timer and self.apgar_timer[seconds] == False:
            print(f"bell ringing at {seconds}")
            self.bell_ring()
            self.apgar_timer[seconds] = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Timer_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

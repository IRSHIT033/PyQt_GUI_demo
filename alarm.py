# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\alarm_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Alarm_widget(object):
    def setupUi(self, Alarm_widget, Mute_alarm):
        Alarm_widget.setObjectName("Alarm_widget")

        Alarm_widget.setStyleSheet("\n"
                                   "#Alarm_widget{\n"
                                   "background:#ffffff;\n"
                                   "border:1px solid #81dbcd;\n"
                                   "border-radius:20px;\n"
                                   "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Alarm_widget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(Alarm_widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "./Assets/thermometer-hot-light.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(Alarm_widget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:#81dbcd;\n"
                                      "border-radius:20px;\n"
                                      "color:#ffffff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Mute_alarm)
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Alarm_widget)
        QtCore.QMetaObject.connectSlotsByName(Alarm_widget)

    def retranslateUi(self, Alarm_widget):
        _translate = QtCore.QCoreApplication.translate
        Alarm_widget.setWindowTitle(_translate("Alarm_widget", "Form"))
        self.label_2.setText(_translate(
            "Alarm_widget", "Temperature High alert!"))
        self.pushButton.setText(_translate("Alarm_widget", "Mute ( For 10s )"))

    def Alarm_Title_Change(self, alarm_text):
        self.label_2.setText(alarm_text)

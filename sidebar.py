# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SideBar(object):
    def setupUi(self, SideBar):
        SideBar.setObjectName("SideBar")
        SideBar.setStyleSheet("background:#4169E1")
        self.verticalLayout = QtWidgets.QVBoxLayout(SideBar)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(SideBar)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setStyleSheet("border-radius:5px;\n"
"border:none;\n"
"background:#ffffff;\n"
"color:#4169E1")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_icon = QtWidgets.QLabel(self.widget)
        self.home_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.home_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.home_icon.setText("")
        self.home_icon.setPixmap(QtGui.QPixmap(".\\UI\\../../../Downloads/house_dark.png"))
        self.home_icon.setScaledContents(True)
        self.home_icon.setObjectName("home_icon")
        self.horizontalLayout.addWidget(self.home_icon)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(SideBar)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settings_icon = QtWidgets.QLabel(self.widget_2)
        self.settings_icon.setMinimumSize(QtCore.QSize(35, 35))
        self.settings_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.settings_icon.setText("")
        self.settings_icon.setPixmap(QtGui.QPixmap(".\\UI\\../../../Downloads/gear_light.png"))
        self.settings_icon.setScaledContents(True)
        self.settings_icon.setObjectName("settings_icon")
        self.horizontalLayout_2.addWidget(self.settings_icon)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#ffffff;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(SideBar)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graph_icon = QtWidgets.QLabel(self.widget_3)
        self.graph_icon.setMinimumSize(QtCore.QSize(35, 35))
        self.graph_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.graph_icon.setText("")
        self.graph_icon.setPixmap(QtGui.QPixmap(".\\UI\\../../../Downloads/chart-line-up_light.png"))
        self.graph_icon.setScaledContents(True)
        self.graph_icon.setObjectName("graph_icon")
        self.horizontalLayout_3.addWidget(self.graph_icon)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#ffffff;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(SideBar)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logs_icon = QtWidgets.QLabel(self.widget_4)
        self.logs_icon.setMinimumSize(QtCore.QSize(35, 35))
        self.logs_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.logs_icon.setText("")
        self.logs_icon.setPixmap(QtGui.QPixmap(".\\UI\\../../../Downloads/notebook_light.png"))
        self.logs_icon.setScaledContents(True)
        self.logs_icon.setObjectName("logs_icon")
        self.horizontalLayout_4.addWidget(self.logs_icon)
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#ffffff;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.widget_4)
        self.label_3 = QtWidgets.QLabel(SideBar)
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(SideBar)
        QtCore.QMetaObject.connectSlotsByName(SideBar)

    def retranslateUi(self, SideBar):
        _translate = QtCore.QCoreApplication.translate
        SideBar.setWindowTitle(_translate("SideBar", "Form"))
        self.label.setText(_translate("SideBar", "Home"))
        self.label_2.setText(_translate("SideBar", "System "))
        self.label_4.setText(_translate("SideBar", "Graph"))
        self.label_5.setText(_translate("SideBar", "logs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SideBar = QtWidgets.QWidget()
    ui = Ui_SideBar()
    ui.setupUi(SideBar)
    SideBar.show()
    sys.exit(app.exec_())

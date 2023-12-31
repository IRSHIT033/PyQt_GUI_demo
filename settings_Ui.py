# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\settings_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from domain.domain_settings import settingsDetailsType


class Ui_settings_screen(object):
    def setupUi(self, settings_screen, settings_details:settingsDetailsType):
        settings_screen.setObjectName("settings_screen")
        settings_screen.resize(723, 542)
        self.settings_details=settings_details
        self.horizontalLayout = QtWidgets.QHBoxLayout(settings_screen)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(settings_screen)
        self.widget.setStyleSheet("background:#ffffff;\n"
"color:#4167e1\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(142, 100))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 138, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.light_level_radiobox = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.light_level_radiobox.setFont(font)
        self.light_level_radiobox.setText("")
        self.light_level_radiobox.setObjectName("light_level_radiobox")
        self.horizontalLayout_2.addWidget(self.light_level_radiobox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.noice_level_radiobox = QtWidgets.QRadioButton(self.widget_3)
        self.noice_level_radiobox.setText("")
        self.noice_level_radiobox.setObjectName("noice_level_radiobox")
        self.horizontalLayout_3.addWidget(self.noice_level_radiobox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(settings_screen)
        self.noice_level_radiobox.setChecked(True)
        self.light_level_radiobox.setChecked(True)

        self.noice_level_radiobox.clicked.connect(self.set_is_noice_level_showing)
        self.light_level_radiobox.clicked.connect(self.set_is_light_level_showing)
        

        QtCore.QMetaObject.connectSlotsByName(settings_screen)

    def set_is_noice_level_showing(self):
        if self.noice_level_radiobox.isChecked():
            self.settings_details.metric.noice_level_shown=True
        else:
            self.settings_details.metric.noice_level_shown=False 

    def set_is_light_level_showing(self):
        if self.light_level_radiobox.isChecked():
            self.settings_details.metric.light_level_shown=True
        else:
            self.settings_details.metric.light_level_shown=False         
              
                

    def retranslateUi(self, settings_screen):
        _translate = QtCore.QCoreApplication.translate
        settings_screen.setWindowTitle(_translate("settings_screen", "Form"))
        self.label_4.setText(_translate("settings_screen", "Settings"))
        self.label_3.setText(_translate("settings_screen", "Metric show"))
        self.label.setText(_translate("settings_screen", "Light Level "))
        self.label_2.setText(_translate("settings_screen", "Noice Level "))

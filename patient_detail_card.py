# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\patient_details_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from domain.domain_patient import PatientDetail


class Ui_patient_detail_card(object):
    def setupUi(self, patient_detail_card, person_data:PatientDetail, current_patient:PatientDetail,header):
        self.person_data=person_data
        patient_detail_card.setObjectName("patient_detail_card")
        patient_detail_card.resize(874, 147)
        self.horizontalLayout = QtWidgets.QHBoxLayout(patient_detail_card)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(patient_detail_card)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 130))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("border:1px solid #4169e1;\n"
"color:#4169e1;\n"
"border-radius:10px;")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border:none;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.set_current_btn = QtWidgets.QPushButton(self.widget_3)
        self.set_current_btn.clicked.connect(lambda: self.setCurrentPatient(self.person_data,header))
        self.set_current_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.set_current_btn.setFont(font)
        self.set_current_btn.setStyleSheet("color:#ffffff;\n"
"background:#4169e1")
        self.set_current_btn.setObjectName("set_current_btn")
        self.gridLayout.addWidget(self.set_current_btn, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_3)

        self.retranslateUi(patient_detail_card)
        QtCore.QMetaObject.connectSlotsByName(patient_detail_card)

    def setCurrentPatient(self,current_patient:PatientDetail,header):
        print(current_patient)
        name="Name: "+ str(current_patient.name)
        header.label_2.setText(name)
        time="Time: "+str(current_patient.time)
        date="Date: "+str(current_patient.date)
        patient_id="Id: "+str(current_patient.patient_Id)
        header.label_3.setText(time)
        header.label_4.setText(date)
        header.label.setText(patient_id)



    def retranslateUi(self, patient_detail_card):
        _translate = QtCore.QCoreApplication.translate
        patient_detail_card.setWindowTitle(_translate("patient_detail_card", "Form"))
        self.label_3.setText(_translate("patient_detail_card", "Weight:"+ str(self.person_data.weight) ))
        self.label_4.setText(_translate("patient_detail_card", "Gender:"+str(self.person_data.gender)))
        self.label_2.setText(_translate("patient_detail_card", "Name:"+self.person_data.name))
        self.label_6.setText(_translate("patient_detail_card", "Date:"+self.person_data.date))
        self.set_current_btn.setText(_translate("patient_detail_card", "Set Current Patient"))
        self.label_5.setText(_translate("patient_detail_card", "Time:"+self.person_data.time))
        self.label.setText(_translate("patient_detail_card", "Patient Id: 1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_patient_detail_card()
    patient1:PatientDetail=PatientDetail(1,"Irshit Mukherjee",80,"12:03","12/02/22","12/3/23",None)
    ui.setupUi(MainWindow,patient1)
    MainWindow.show()
    sys.exit(app.exec_())
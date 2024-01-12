from PyQt5 import QtCore, QtGui, QtWidgets    
from alarm_logs_Ui import Ui_alarm_logs
from domain.domain_patient import PatientDetail, alarm_log
from graph_Ui import Graph_Screen_UI
from header_Ui import Ui_Header
from person_data import Ui_person_history
from settings_Ui import Ui_settings_screen
from sidebar import Ui_SideBar
import websocket_handler
import set_temp
from modes_Ui import Ui_mode_screen
from domain.domain_settings import metricDetailsType, settingsDetailsType
import alarm
import timer_ui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 900)
        MainWindow.setStyleSheet("#main_screen{\n"
                                 "background:#ffffff;\n"
                                 "}\n"
                                 "\n"
                                 "#Header{\n"
                                 "   background-color:#ffffff;\n"
                                
                                 "}\n"
                                 "\n"
                                 "#baby_temp_div, #set_temp_div, #Power_preheat, #baby_tmp_preheat\n"
                                 "#light_level, #noice_level {\n"
                                 "   border:0.8px solid #4169E1;\n"
                                 "   border-radius:25px;\n"
                                 " background:#ffffff;\n"
                                 "}\n"
                                 "\n"
                                 "#auto_btn, #manual_btn, #preheat_btn{\n"
                                 "border-radius:25px;\n"
                                 "background-color:#4169E1;\n"
                                 "color:#f4f4f5;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
         
        # Mock Ups-------------------------------------------- #
        self.Patient_details: list[PatientDetail]=[]

        # self.patient1:PatientDetail=PatientDetail(1,"Irshit Mukherjee",80,"12:03","12/02/22",[alarm_log(log_message="Temperature Hot",time="12 : 03 am",date="12 / 02 / 22"),
        #                                                                             alarm_log(log_message="Temperature Low",time="12 : 31 am",date="12 / 02 / 22")
        #                                                                             ])
        
        # self.patient2:PatientDetail=PatientDetail(1,"Aritra Roy",67,"12:03","12/02/22",[alarm_log(log_message="Temperature Hot",time="10 : 03 pm",date="12 / 02 / 22")])
        
        # self.person_data: list[PatientDetail]
        # self.person_data.append(self.patient1)
        # self.person_data.append(self.patient2)
        
        # ------------------------------------------------------ #

        self.system_settings : settingsDetailsType = settingsDetailsType(metric=metricDetailsType(light_level_shown=True,noice_level_shown=True))

        # handling websockets
        self.websocketHandler = websocket_handler.WebSocketHandler()
        self.websocketHandler.messageReceived.connect(self.showAlarm)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.header_container=QtWidgets.QWidget(self.centralwidget)
        self.Header = QtWidgets.QWidget(self.header_container)
 
        self.Header_UI=Ui_Header()
        self.Header_UI.setupUi(self.Header)
        self.Header.show()

        self.verticalLayout.addWidget(self.Header)

        self.Main_screen_container = QtWidgets.QWidget(self.centralwidget)
        self.Main_screen_container.setObjectName("Main_screen_container")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.Main_screen_container)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stacked_pages_container = QtWidgets.QWidget(
            self.Main_screen_container)
        self.stacked_pages_container.setStyleSheet("#stacked_pages_container{\n"
                                                   "background:#ffffff;\n"
                                                   "}")
        self.stacked_pages_container.setObjectName("stacked_pages_container")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
            self.stacked_pages_container)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.main_screen = QtWidgets.QStackedWidget(
            self.stacked_pages_container)
        
        self.main_screen.setObjectName("main_screen")
        
        # -------------------------Home screeen----------------------#
        self.modes_widget=QtWidgets.QWidget()
        self.modes_ui=Ui_mode_screen()
        self.modes_ui.setupUi(self.modes_widget)
        self.modes_widget.show()
        self.main_screen.addWidget(self.modes_widget)
        # -----------------------------------------------------------#
       

        #------------alarm_data_logs---------#
        self.alarmlogs_screen = QtWidgets.QWidget()
        self.alarmlogs_ui =  Ui_alarm_logs()
        self.alarmlogs_ui.setupUi(self.alarmlogs_screen)
        self.alarmlogs_screen.show()
        self.main_screen.addWidget(self.alarmlogs_screen)

        # -----------------------------------------------------------#



        # -------------------------Settings screeen------------------#
        self.settings_screen=QtWidgets.QWidget()
        self.settings_ui=Ui_settings_screen()
        self.settings_ui.setupUi(self.settings_screen,self.system_settings)
        self.settings_screen.show()
        self.main_screen.addWidget(self.settings_screen)

        # -----------------------------------------------------------#        
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.graph_ui = Graph_Screen_UI()
        self.graph_ui.setupUi(self.graph_page)
        self.graph_page.show()
        self.main_screen.addWidget(self.graph_page)

        self.horizontalLayout_8.addWidget(self.main_screen)
        self.horizontalLayout.addWidget(self.stacked_pages_container)

         #------------person_data_logs---------#
        self.personlogs_screen = QtWidgets.QWidget()
        self.personlogs_ui =  Ui_person_history()

        self.personlogs_ui.setupUi(self.personlogs_screen, self.Patient_details)
        self.personlogs_screen.show()
        self.main_screen.addWidget(self.personlogs_screen)

        self.right_sidebar = QtWidgets.QWidget(self.Main_screen_container)
        self.right_sidebar.resize(1000,1000)
        self.sidebar_ui = Ui_SideBar()
        self.sidebar_ui.setupUi(self.right_sidebar,self)
        self.right_sidebar.show()
        
        # sidebar navigation
        self.sidebar_ui.widget.mouseReleaseEvent=self.showHomeScreen
        self.sidebar_ui.widget_4.mouseReleaseEvent=self.showLogsScreen
        self.sidebar_ui.widget_2.mouseReleaseEvent=self.showSettingsScreen
        self.sidebar_ui.widget_5.mouseReleaseEvent=self.showDataScreen
        self.sidebar_ui.widget_3.mouseReleaseEvent=self.showGraphScreen
        #
        
        self.horizontalLayout.addWidget(self.right_sidebar)
        self.verticalLayout.addWidget(self.Main_screen_container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_screen.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_persons_data(self):
        self.stackedWidget.setCurrentIndex(1)
        self.human_data_btn.setStyleSheet(
            "border-radius:10px;\n"
            "background:#4169E1;\n"
            "border:1px solid #4169E1;\n"
            "color:#ffffff;"
        )
        self.alarm_log_btn.setStyleSheet(
            "border-radius:10px;\n"
            "background:#ffffff;\n"
            "border:1px solid #4169E1;\n"
            "color:#4169E1;"
        )

    def show_alarms_log(self):
        self.stackedWidget.setCurrentIndex(0)
        self.human_data_btn.setStyleSheet(
            "border-radius:10px;\n"
            "background:#ffffff;\n"
            "border:1px solid #4169E1;\n"
            "color:#4169E1;"

        )
        self.alarm_log_btn.setStyleSheet(
            "border-radius:10px;\n"
            "background:#4169E1;\n"
            "border:1px solid #4169E1;\n"
            "color:#ffffff;"
        )

    def SetTemperature(self):
        Dialog = QtWidgets.QDialog(self.centralwidget)
        ui = set_temp.SetTemp_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()

    def SetAutoMode(self):
        self.ModeStackedWindow.setCurrentIndex(2)
        self.auto_btn.setStyleSheet("background:#4169E1;\n"
                                    "color:#ffffff\n")
        self.manual_btn.setStyleSheet("border-radius:25px;\n"
                                      "background:#ffffff;\n"
                                      "border:1px solid #4169E1;\n"
                                      "color:#4169E1;")
        self.preheat_btn.setStyleSheet("border-radius:25px;\n"
                                       "background:#ffffff;\n"
                                       "border:1px solid #4169E1;\n"
                                       "color:#4169E1;")

    def SetManualMode(self):
        self.ModeStackedWindow.setCurrentIndex(0)
        self.manual_btn.setStyleSheet("background:#4169E1;\n"
                                      "color:#ffffff\n")
        self.preheat_btn.setStyleSheet("border-radius:25px;\n"
                                       "background:#ffffff;\n"
                                       "border:1px solid #4169E1;\n"
                                       "color:#4169E1;")
        self.auto_btn.setStyleSheet("border-radius:25px;\n"
                                    "background:#ffffff;\n"
                                    "border:1px solid #4169E1;\n"
                                    "color:#4169E1;")

    def SetPreheatMode(self):
        self.ModeStackedWindow.setCurrentIndex(1)
        self.preheat_btn.setStyleSheet("background:#4169E1;\n"
                                       "color:#ffffff\n")
        self.manual_btn.setStyleSheet("border-radius:25px;\n"
                                      "background:#ffffff;\n"
                                      "border:1px solid #4169E1;\n"
                                      "color:#4169E1;")
        self.auto_btn.setStyleSheet("border-radius:25px;\n"
                                    "background:#ffffff;\n"
                                    "border:1px solid #4169E1;\n"
                                    "color:#4169E1;")

    def showAlarm(self, alarm_title):
        self.Alarm_widget.show()
        self.alarm_ui.Alarm_Title_Change(alarm_title)

    def showHomeScreen(self, event):
        self.main_screen.setCurrentIndex(0)
        self.sidebar_ui.widget.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#ffffff;\n"
        "color:#4169e1")
        self.sidebar_ui.widget_2.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_3.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_4.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_5.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#4167e1;\n"
        "color:#ffffff")
        self.sidebar_ui.logs_icon.setPixmap(QtGui.QPixmap("./Assets/notebook_light.png"))
        self.sidebar_ui.home_icon.setPixmap(QtGui.QPixmap("./Assets/house_dark.png"))
        self.sidebar_ui.settings_icon.setPixmap(QtGui.QPixmap("./Assets/gear_light.png"))
        self.sidebar_ui.graph_icon.setPixmap(QtGui.QPixmap("./Assets/chart-line-up_light.png"))
        self.sidebar_ui.person_icon.setPixmap(QtGui.QPixmap("./Assets/user-square_light.png"))
        self.sidebar_ui.label.setStyleSheet("color:#4169e1")
        self.sidebar_ui.label_2.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_4.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_5.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_6.setStyleSheet("color:#ffffff")

        if self.system_settings.metric.light_level_shown == False and self.system_settings.metric.noice_level_shown == False:
           self.modes_ui.noice_leve_manual_widget.hide()
           self.modes_ui.noice_level_auto_widget.hide()
           self.modes_ui.widget_7.hide()
           self.modes_ui.light_level_widget.hide()
           self.modes_ui.light_level_auto_widget.hide()
           self.modes_ui.widget_8.hide()
           self.modes_ui.widget_16.hide()

        elif self.system_settings.metric.light_level_shown == False:
           self.modes_ui.light_level_widget.hide()
           self.modes_ui.light_level_auto_widget.hide()
           self.modes_ui.widget_8.hide()

        elif self.system_settings.metric.noice_level_shown == False:
           self.modes_ui.noice_leve_manual_widget.hide()
           self.modes_ui.noice_level_auto_widget.hide()
           self.modes_ui.widget_7.hide()

        if self.system_settings.metric.light_level_shown == True and self.system_settings.metric.noice_level_shown == True: 
           self.modes_ui.noice_leve_manual_widget.show()
           self.modes_ui.noice_level_auto_widget.show()
           self.modes_ui.widget_8.show()

           self.modes_ui.light_level_widget.show()
           self.modes_ui.light_level_auto_widget.show()
           self.modes_ui.widget_7.show() 
           
           self.modes_ui.widget_16.show()

        elif self.system_settings.metric.light_level_shown == True :
           self.modes_ui.light_level_widget.show()
           self.modes_ui.light_level_auto_widget.show()
           self.modes_ui.widget_8.show()

        elif self.system_settings.metric.noice_level_shown == True :
           self.modes_ui.noice_leve_manual_widget.show()
           self.modes_ui.noice_level_auto_widget.show()
           self.modes_ui.widget_7.show()      
         
    def showGraphScreen(self,event):
        self.main_screen.setCurrentIndex(3)

        self.sidebar_ui.widget.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_2.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_3.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#ffffff;\n"
        "color:#4169E1")
        self.sidebar_ui.widget_4.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_5.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#4167e1;\n"
        "color:#ffffff")

        self.sidebar_ui.logs_icon.setPixmap(QtGui.QPixmap("./Assets/notebook_light.png"))
        self.sidebar_ui.home_icon.setPixmap(QtGui.QPixmap("./Assets/house_light.png"))
        self.sidebar_ui.settings_icon.setPixmap(QtGui.QPixmap("./Assets/gear_light.png"))
        self.sidebar_ui.graph_icon.setPixmap(QtGui.QPixmap("./Assets/chart-line-up_dark.png"))
        self.sidebar_ui.person_icon.setPixmap(QtGui.QPixmap("./Assets/user-square_light.png"))

        self.sidebar_ui.label.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_2.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_4.setStyleSheet("color:#4167e1")
        self.sidebar_ui.label_6.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_5.setStyleSheet("color:#ffffff")
    
    
    def showLogsScreen(self,event):
        self.main_screen.setCurrentIndex(1)
        self.sidebar_ui.widget.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_2.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_3.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_4.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#ffffff;\n"
        "color:#4169E1")
        self.sidebar_ui.widget_5.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
        "background:#4167e1;\n"
        "color:#ffffff")

        self.sidebar_ui.logs_icon.setPixmap(QtGui.QPixmap("./Assets/notebook_dark.png"))
        self.sidebar_ui.home_icon.setPixmap(QtGui.QPixmap("./Assets/house_light.png"))
        self.sidebar_ui.settings_icon.setPixmap(QtGui.QPixmap("./Assets/gear_light.png"))
        self.sidebar_ui.graph_icon.setPixmap(QtGui.QPixmap("./Assets/chart-line-up_light.png"))
        self.sidebar_ui.person_icon.setPixmap(QtGui.QPixmap("./Assets/user-square_light.png"))

        self.sidebar_ui.label.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_2.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_4.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_6.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_5.setStyleSheet("color:#4169e1")

    def showSettingsScreen(self, event):
        self.main_screen.setCurrentIndex(2)
        self.sidebar_ui.widget.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_2.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#ffffff;\n"
        "color:#4169e1")
        self.sidebar_ui.widget_3.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_4.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_5.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.logs_icon.setPixmap(QtGui.QPixmap("./Assets/notebook_light.png"))
        self.sidebar_ui.home_icon.setPixmap(QtGui.QPixmap("./Assets/house_light.png"))
        self.sidebar_ui.settings_icon.setPixmap(QtGui.QPixmap("./Assets/gear_dark.png"))
        self.sidebar_ui.graph_icon.setPixmap(QtGui.QPixmap("./Assets/chart-line-up_light.png"))
        self.sidebar_ui.person_icon.setPixmap(QtGui.QPixmap("./Assets/user-square_light.png"))
        self.sidebar_ui.label.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_2.setStyleSheet("color:#4167e1")
        self.sidebar_ui.label_4.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_5.setStyleSheet("color:#ffffff") 
        self.sidebar_ui.label_6.setStyleSheet("color:#ffffff") 

    def showDataScreen(self, event):
        self.main_screen.setCurrentIndex(4)
        self.sidebar_ui.widget.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_2.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_3.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_4.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#4169E1;\n"
        "color:#ffffff")
        self.sidebar_ui.widget_5.setStyleSheet("border-radius:5px;\n"
        "border:none;\n"
         "background:#ffffff;\n"
        "color:#4169e1")

        self.sidebar_ui.logs_icon.setPixmap(QtGui.QPixmap("./Assets/notebook_light.png"))
        self.sidebar_ui.home_icon.setPixmap(QtGui.QPixmap("./Assets/house_light.png"))
        self.sidebar_ui.settings_icon.setPixmap(QtGui.QPixmap("./Assets/gear_light.png"))
        self.sidebar_ui.graph_icon.setPixmap(QtGui.QPixmap("./Assets/chart-line-up_light.png"))
        self.sidebar_ui.person_icon.setPixmap(QtGui.QPixmap("./Assets/user-square_dark.png"))

        self.sidebar_ui.label.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_6.setStyleSheet("color:#4167e1")
        self.sidebar_ui.label_4.setStyleSheet("color:#ffffff")
        self.sidebar_ui.label_5.setStyleSheet("color:#ffffff")        
        self.sidebar_ui.label_2.setStyleSheet("color:#ffffff")        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

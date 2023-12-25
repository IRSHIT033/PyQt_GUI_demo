from PyQt5 import QtCore, QtGui, QtWidgets
from sidebar import Ui_SideBar
import websocket_handler
import set_temp
import alarm
import timer_ui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 900)
        MainWindow.setStyleSheet("#cprtime_nav_item ,#alarm_nav_item, #apgartime_nav_item, #logs_nav_item, #graph_nav_item{\n"
                                 "   border:0.8px solid #4169E1;\n"
                                 "   border-radius:25px;\n"
                                 "   background-color:#ffffff;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "#main_screen{\n"
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

        # handling websockets
        self.websocketHandler = websocket_handler.WebSocketHandler()
        self.websocketHandler.messageReceived.connect(self.showAlarm)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.Header = QtWidgets.QWidget(self.centralwidget)
        # self.Header.setMinimumSize(QtCore.QSize(0, 120))
        # self.Header.setMaximumSize(QtCore.QSize(16777215, 120))
        # font = QtGui.QFont()
        # font.setPointSize(30)
        # self.Header.setFont(font)
        # self.Header.setObjectName("Header")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header)
        # self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_2.setSpacing(0)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.date_widget = QtWidgets.QWidget(self.Header)
        # self.date_widget.setObjectName("date_widget")
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.date_widget)
        # self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        # self.horizontalLayout_3.setSpacing(12)
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.date_icon = QtWidgets.QLabel(self.date_widget)
        # self.date_icon.setMaximumSize(QtCore.QSize(30, 30))
        # self.date_icon.setBaseSize(QtCore.QSize(20, 20))
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # font.setKerning(True)
        # self.date_icon.setFont(font)
        # self.date_icon.setText("")
        # self.date_icon.setPixmap(QtGui.QPixmap(
        #     "./Assets/date_range.png"))
        # self.date_icon.setScaledContents(True)
        # self.date_icon.setObjectName("date_icon")
        # self.horizontalLayout_3.addWidget(
        #     self.date_icon, 0, QtCore.Qt.AlignVCenter)
        # self.date_text = QtWidgets.QLabel(self.date_widget)
        # self.date_text.setMaximumSize(QtCore.QSize(150, 16777215))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # font.setBold(False)
        # font.setWeight(50)
        # self.date_text.setFont(font)
        # self.date_text.setScaledContents(False)
        # self.date_text.setWordWrap(True)
        # self.date_text.setObjectName("date_text")
        # self.horizontalLayout_3.addWidget(self.date_text)
        # self.time_icon = QtWidgets.QLabel(self.date_widget)
        # self.time_icon.setMaximumSize(QtCore.QSize(30, 30))
        # self.time_icon.setText("")
        # self.time_icon.setPixmap(QtGui.QPixmap(
        #     "./Assets/access_time.png"))
        # self.time_icon.setScaledContents(True)
        # self.time_icon.setObjectName("time_icon")
        # self.horizontalLayout_3.addWidget(
        #     self.time_icon, 0, QtCore.Qt.AlignVCenter)
        # self.time_text = QtWidgets.QLabel(self.date_widget)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # font.setBold(False)
        # font.setWeight(50)
        # self.time_text.setFont(font)
        # self.time_text.setObjectName("time_text")
        # self.horizontalLayout_3.addWidget(self.time_text)

        # # setup UI for timer
        # self.timerUI = timer_ui.Timer_UI()
        # self.timerUI.setupUi(self.date_widget)

        # self.horizontalLayout_3.addWidget(
        #     self.timerUI.widget_11, 0, QtCore.Qt.AlignHCenter)

        # self.horizontalLayout_2.addWidget(self.date_widget)
        #self.verticalLayout.addWidget(self.Header)
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
        self.main_screen.setStyleSheet("#home_page{\n"
                                       "background:#ffffff;\n"
                                       "}")
        self.main_screen.setObjectName("main_screen")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        # self.verticalLayout_7.addWidget()
        # self.alarmModal=alarm_widget.Ui_Alarm_widget
        self.home_page.setContentsMargins(20, 0, 0, 0)
        self.Alarm_widget = QtWidgets.QWidget()
        self.alarm_ui = alarm.Ui_Alarm_widget()
        self.alarm_ui.setupUi(
            self.Alarm_widget, self.websocketHandler.SendMessage)
        self.Alarm_widget.hide()
        self.Alarm_widget.setContentsMargins(10, 0, 10, 20)
        self.verticalLayout_7.addWidget(self.Alarm_widget)

        self.mode_customized_container = QtWidgets.QWidget(self.home_page)
        self.mode_customized_container.setMinimumSize(QtCore.QSize(0, 0))
        self.mode_customized_container.setObjectName(
            "mode_customized_container")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(
            self.mode_customized_container)
        self.verticalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.ModeStackedWindow = QtWidgets.QStackedWidget(
            self.mode_customized_container)
        self.ModeStackedWindow.setMinimumSize(QtCore.QSize(0, 257))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.ModeStackedWindow.setFont(font)
        self.ModeStackedWindow.setStyleSheet("color:#4169E1;\n"
                                             "background:#ffffff")
        self.ModeStackedWindow.setObjectName("ModeStackedWindow")
        self.ManualMode = QtWidgets.QWidget()
        self.ManualMode.setObjectName("ManualMode")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.ManualMode)
        self.horizontalLayout_9.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_5 = QtWidgets.QWidget(self.ManualMode)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)

        self.baby_temp_div = QtWidgets.QWidget(self.widget_5)
        self.baby_temp_div.setMinimumSize(QtCore.QSize(0, 257))
        self.baby_temp_div.setObjectName("baby_temp_div")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.baby_temp_div)
        self.horizontalLayout_24.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout_24.setSpacing(4)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem)
        self.label_11 = QtWidgets.QLabel(self.baby_temp_div)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_24.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.baby_temp_div)
        self.pushButton = QtWidgets.QPushButton(self.widget_5)
        self.pushButton.setMinimumSize(QtCore.QSize(350, 65))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton.clicked.connect(self.SetTemperature)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#4169E1;\n"
                                      "color:#ffffff;\n"
                                      "border-radius:25px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/thermometer-bold.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.horizontalLayout_9.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.ManualMode)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Temp_container_3 = QtWidgets.QWidget(self.widget_3)
        self.Temp_container_3.setMinimumSize(QtCore.QSize(400, 0))
        self.Temp_container_3.setStyleSheet("#light_level_div_2, #noice_div_2, #power_div_2 {\n"
                                            "border-radius:25px;\n"
                                            "border:1px solid #4169E1;\n"
                                            "}")
        self.Temp_container_3.setObjectName("Temp_container_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.Temp_container_3)
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_41 = QtWidgets.QLabel(self.Temp_container_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setWordWrap(True)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_21.addWidget(self.label_41)
        self.noice_div_2 = QtWidgets.QWidget(self.Temp_container_3)
        self.noice_div_2.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noice_div_2.setFont(font)
        self.noice_div_2.setObjectName("noice_div_2")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.noice_div_2)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.manual_noice_label = QtWidgets.QLabel(self.noice_div_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.manual_noice_label.setFont(font)
        self.manual_noice_label.setObjectName("manual_noice_label")
        self.horizontalLayout_37.addWidget(
            self.manual_noice_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_21.addWidget(self.noice_div_2)
        self.label_43 = QtWidgets.QLabel(self.Temp_container_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setWordWrap(True)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_21.addWidget(self.label_43)
        self.light_level_div_2 = QtWidgets.QWidget(self.Temp_container_3)
        self.light_level_div_2.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.light_level_div_2.setFont(font)
        self.light_level_div_2.setStyleSheet("#light_level{\n"
                                             "   border-radius: 25px;\n"
                                             "     border:1px solid #4169E1;\n"
                                             "background:#ffffff\n"
                                             "}")
        self.light_level_div_2.setObjectName("light_level_div_2")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(
            self.light_level_div_2)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.manual_light_label = QtWidgets.QLabel(self.light_level_div_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.manual_light_label.setFont(font)
        self.manual_light_label.setStyleSheet("")
        self.manual_light_label.setObjectName("manual_light_label")
        self.horizontalLayout_38.addWidget(
            self.manual_light_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_21.addWidget(self.light_level_div_2)
        self.label_45 = QtWidgets.QLabel(self.Temp_container_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_21.addWidget(self.label_45)
        self.power_div_2 = QtWidgets.QWidget(self.Temp_container_3)
        self.power_div_2.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.power_div_2.setFont(font)
        self.power_div_2.setStyleSheet("#light_level{\n"
                                       "   border-radius: 25px;\n"
                                       "     border:1px solid #4169E1;\n"
                                       "background:#ffffff\n"
                                       "}")
        self.power_div_2.setObjectName("power_div_2")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.power_div_2)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.manual_power_label = QtWidgets.QLabel(self.power_div_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.manual_power_label.setFont(font)
        self.manual_power_label.setStyleSheet("")
        self.manual_power_label.setObjectName("manual_power_label")
        self.horizontalLayout_39.addWidget(
            self.manual_power_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_21.addWidget(self.power_div_2)
        self.verticalLayout_11.addWidget(self.Temp_container_3)
        self.horizontalLayout_9.addWidget(self.widget_3)
        self.ModeStackedWindow.addWidget(self.ManualMode)
        self.PreheatMode = QtWidgets.QWidget()
        self.PreheatMode.setObjectName("PreheatMode")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.PreheatMode)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.Heat_container = QtWidgets.QWidget(self.PreheatMode)
        self.Heat_container.setStyleSheet("")
        self.Heat_container.setObjectName("Heat_container")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.Heat_container)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_28 = QtWidgets.QLabel(self.Heat_container)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_15.addWidget(self.label_28)
        self.Power_preheat = QtWidgets.QWidget(self.Heat_container)
        self.Power_preheat.setMinimumSize(QtCore.QSize(0, 257))
        self.Power_preheat.setObjectName("Power_preheat")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Power_preheat)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_15 = QtWidgets.QWidget(self.Power_preheat)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_16 = QtWidgets.QWidget(self.widget_15)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_23 = QtWidgets.QLabel(self.widget_16)
        self.label_23.setMinimumSize(QtCore.QSize(85, 85))
        self.label_23.setMaximumSize(QtCore.QSize(85, 85))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("./Assets/fire-light (1).png"))
        self.label_23.setScaledContents(True)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_28.addWidget(self.label_23)
        self.verticalLayout_17.addWidget(self.widget_16)
        self.label_24 = QtWidgets.QLabel(self.widget_15)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.verticalLayout_16.addWidget(
            self.widget_15, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout_15.addWidget(self.Power_preheat)
        self.horizontalLayout_26.addWidget(self.Heat_container)
        self.Temp_container = QtWidgets.QWidget(self.PreheatMode)
        self.Temp_container.setStyleSheet("")
        self.Temp_container.setObjectName("Temp_container")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Temp_container)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.Temp_container)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_14.addWidget(self.label_27)
        self.noice_level = QtWidgets.QWidget(self.Temp_container)
        self.noice_level.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noice_level.setFont(font)
        self.noice_level.setObjectName("noice_level")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.noice_level)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_25 = QtWidgets.QLabel(self.noice_level)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_27.addWidget(
            self.label_25, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_14.addWidget(self.noice_level)
        self.label_29 = QtWidgets.QLabel(self.Temp_container)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_14.addWidget(self.label_29)
        self.light_level = QtWidgets.QWidget(self.Temp_container)
        self.light_level.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.light_level.setFont(font)
        self.light_level.setStyleSheet("#light_level{\n"
                                       "   border-radius: 25px;\n"
                                       "     border:1px solid #4169E1;\n"
                                       "background:#ffffff\n"
                                       "}")
        self.light_level.setObjectName("light_level")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.light_level)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_26 = QtWidgets.QLabel(self.light_level)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background:#ffffff;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_29.addWidget(
            self.label_26, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_14.addWidget(self.light_level)
        self.horizontalLayout_26.addWidget(self.Temp_container)
        self.ModeStackedWindow.addWidget(self.PreheatMode)
        self.AutoMode = QtWidgets.QWidget()
        self.AutoMode.setStyleSheet("#baby_tmp_container, #light_level_div, #power_div, #noice_div{\n"
                                    "background:#ffffff;\n"
                                    "border-radius:25px;\n"
                                    "border: 1px solid #82dbcd;\n"
                                    "}")
        self.AutoMode.setObjectName("AutoMode")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.AutoMode)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.widget_13 = QtWidgets.QWidget(self.AutoMode)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.widget_18 = QtWidgets.QWidget(self.widget_13)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(12)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_34 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_20.addWidget(self.label_34, 0, QtCore.Qt.AlignTop)
        self.baby_tmp_container = QtWidgets.QWidget(self.widget_18)
        self.baby_tmp_container.setMinimumSize(QtCore.QSize(404, 257))
        self.baby_tmp_container.setObjectName("baby_tmp_container")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(
            self.baby_tmp_container)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.widget_17 = QtWidgets.QWidget(self.baby_tmp_container)
        self.widget_17.setStyleSheet("   border-radius: 25px;\n"
                                     "     border:1px solid #4169E1;\n"
                                     "background:#ffffff")
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem2)
        self.label_38 = QtWidgets.QLabel(self.widget_17)
        self.label_38.setStyleSheet("border:none")
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("./Assets/baby-light.png"))
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_36.addWidget(self.label_38)
        self.label_35 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("border:none;")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_36.addWidget(self.label_35)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem3)
        self.horizontalLayout_35.addWidget(self.widget_17)
        self.verticalLayout_20.addWidget(
            self.baby_tmp_container, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_2.setMinimumSize(QtCore.QSize(350, 65))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 65))
        self.pushButton_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#4169E1;\n"
                                        "color:#ffffff;\n"
                                        "border-radius:25px;")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_20.addWidget(self.pushButton_2)
        self.horizontalLayout_33.addWidget(self.widget_18)
        self.horizontalLayout_30.addWidget(self.widget_13)
        self.widget = QtWidgets.QWidget(self.AutoMode)
        self.widget.setObjectName("widget")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Temp_container_2 = QtWidgets.QWidget(self.widget)
        self.Temp_container_2.setStyleSheet("")
        self.Temp_container_2.setObjectName("Temp_container_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.Temp_container_2)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_30 = QtWidgets.QLabel(self.Temp_container_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_19.addWidget(self.label_30)
        self.noice_div = QtWidgets.QWidget(self.Temp_container_2)
        self.noice_div.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.noice_div.setFont(font)
        self.noice_div.setObjectName("noice_div")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.noice_div)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_31 = QtWidgets.QLabel(self.noice_div)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_31.addWidget(
            self.label_31, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addWidget(self.noice_div)
        self.label_32 = QtWidgets.QLabel(self.Temp_container_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_19.addWidget(self.label_32)
        self.light_level_div = QtWidgets.QWidget(self.Temp_container_2)
        self.light_level_div.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.light_level_div.setFont(font)
        self.light_level_div.setStyleSheet("#light_level{\n"
                                           "   border-radius: 25px;\n"
                                           "     border:1px solid #4169E1;\n"
                                           "background:#ffffff\n"
                                           "}")
        self.light_level_div.setObjectName("light_level_div")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.light_level_div)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_33 = QtWidgets.QLabel(self.light_level_div)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_32.addWidget(
            self.label_33, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addWidget(self.light_level_div)
        self.label_36 = QtWidgets.QLabel(self.Temp_container_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_19.addWidget(self.label_36)
        self.power_div = QtWidgets.QWidget(self.Temp_container_2)
        self.power_div.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.power_div.setFont(font)
        self.power_div.setStyleSheet("#light_level{\n"
                                     "   border-radius: 25px;\n"
                                     "     border:1px solid #4169E1;\n"
                                     "background:#ffffff\n"
                                     "}")
        self.power_div.setObjectName("power_div")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.power_div)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_37 = QtWidgets.QLabel(self.power_div)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("")
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_34.addWidget(
            self.label_37, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addWidget(self.power_div)
        self.verticalLayout_18.addWidget(self.Temp_container_2)
        self.horizontalLayout_30.addWidget(self.widget)
        self.ModeStackedWindow.addWidget(self.AutoMode)
        self.verticalLayout_12.addWidget(self.ModeStackedWindow)
        self.mode_text_container = QtWidgets.QWidget(
            self.mode_customized_container)
        self.mode_text_container.setMinimumSize(QtCore.QSize(0, 60))
        self.mode_text_container.setStyleSheet("\n"
                                               "    background-color:#f4f4f5;\n"
                                               "    border-radius:10px;")
        self.mode_text_container.setObjectName("mode_text_container")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(
            self.mode_text_container)
        self.horizontalLayout_12.setContentsMargins(15, 15, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.mode_text = QtWidgets.QLabel(self.mode_text_container)
        self.mode_text.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mode_text.setFont(font)
        self.mode_text.setStyleSheet("")
        self.mode_text.setObjectName("mode_text")
        self.horizontalLayout_12.addWidget(
            self.mode_text, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.mode_text_container)
        self.widget_2 = QtWidgets.QWidget(self.mode_customized_container)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 75))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.auto_btn = QtWidgets.QPushButton(self.widget_2)
        self.auto_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.auto_btn.setFont(font)
        self.auto_btn.clicked.connect(self.SetAutoMode)
        self.auto_btn.setStyleSheet("border-radius:25px;\n"
                                    "background:#ffffff;\n"
                                    "border:1px solid #4169E1;\n"
                                    "color:#4169E1;")
        self.auto_btn.setObjectName("auto_btn")
        self.horizontalLayout_11.addWidget(self.auto_btn)
        self.manual_btn = QtWidgets.QPushButton(self.widget_2)
        self.manual_btn.clicked.connect(self.SetManualMode)
        self.manual_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.manual_btn.setFont(font)
        self.manual_btn.setStyleSheet("border-radius:25px;")
        self.manual_btn.setObjectName("manual_btn")
        self.horizontalLayout_11.addWidget(self.manual_btn)
        self.preheat_btn = QtWidgets.QPushButton(self.widget_2)
        self.preheat_btn.clicked.connect(self.SetPreheatMode)
        self.preheat_btn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.preheat_btn.setFont(font)
        self.preheat_btn.setStyleSheet("border-radius:25px;\n"
                                       "background:#ffffff;\n"
                                       "border:1px solid #4169E1;\n"
                                       "color:#4169E1;")
        self.preheat_btn.setObjectName("preheat_btn")
        self.horizontalLayout_11.addWidget(self.preheat_btn)
        self.verticalLayout_12.addWidget(
            self.widget_2, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_7.addWidget(
            self.mode_customized_container, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.home_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7.addWidget(self.frame)
        self.main_screen.addWidget(self.home_page)

        # -------------------------logs screeen----------------------#
        self.logs_page = QtWidgets.QWidget()
        self.logs_page.setStyleSheet("background-color:#ffffff;")
        self.logs_page.setObjectName("logs_page")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.logs_page)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_22 = QtWidgets.QWidget(self.logs_page)
        self.widget_22.setMinimumSize(QtCore.QSize(500, 60))
        self.widget_22.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_22)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.human_data_btn = QtWidgets.QPushButton(self.widget_22)
        self.human_data_btn.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.human_data_btn.setFont(font)
        self.human_data_btn.setStyleSheet("border-radius:10px;\n"
                                          "background:#4169E1;\n"
                                          "border:1px solid #4169E1;\n"
                                          "color:#ffffff;")
        self.human_data_btn.setObjectName("human_data_btn")
        self.human_data_btn.clicked.connect(self.show_persons_data)
        self.horizontalLayout_14.addWidget(self.human_data_btn)
        self.alarm_log_btn = QtWidgets.QPushButton(self.widget_22)
        self.alarm_log_btn.setMaximumSize(QtCore.QSize(200, 60))
        self.alarm_log_btn.clicked.connect(self.show_alarms_log)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.alarm_log_btn.setFont(font)
        self.alarm_log_btn.setStyleSheet("border-radius:10px;\n"
                                         "background:#ffffff;\n"
                                         "border:1px solid #4169E1;\n"
                                         "color:#4169E1;")
        self.alarm_log_btn.setObjectName("alarm_log_btn")
        self.horizontalLayout_14.addWidget(self.alarm_log_btn)
        self.verticalLayout_13.addWidget(
            self.widget_22, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget = QtWidgets.QStackedWidget(self.logs_page)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.alarm_logs = QtWidgets.QWidget()
        self.alarm_logs.setObjectName("alarm_logs")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.alarm_logs)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.alarm_logs)
        self.scrollArea_2.setStyleSheet("border:none")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 946, 683))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.alarm = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.alarm.setMaximumSize(QtCore.QSize(16777215, 80))
        self.alarm.setStyleSheet("#alarm{\n"
                                 "border:1px solid #4169E1;\n"
                                 "border-radius:15px;\n"
                                 "}")
        self.alarm.setObjectName("alarm")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.alarm)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.alarm)
        self.label_13.setMaximumSize(QtCore.QSize(60, 60))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(
            "./Assets/thermometer-hot-light.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.label_14 = QtWidgets.QLabel(self.alarm)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_16.addWidget(self.label_14)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.widget_14 = QtWidgets.QWidget(self.alarm)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_15 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_25.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_25.addWidget(self.label_16)
        self.horizontalLayout_16.addWidget(self.widget_14)
        self.verticalLayout_28.addWidget(self.alarm)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.alarm_logs)
        self.human_data = QtWidgets.QWidget()
        self.human_data.setObjectName("human_data")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.human_data)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.widget_4 = QtWidgets.QWidget(self.human_data)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background:#808080;\n"
                                        "border-radius:10px;\n"
                                        "color:#ffffff")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_15.addWidget(self.pushButton_5)
        self.verticalLayout_23.addWidget(self.widget_4)
        self.scrollArea = QtWidgets.QScrollArea(self.human_data)
        self.scrollArea.setStyleSheet("border:none")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 946, 535))
        self.scrollAreaWidgetContents.setStyleSheet("#Patientdetails{\n"
                                                    "border-radius:10px;\n"
                                                    "border:1px solid #4169E1;\n"
                                                    "color:#808080;\n"
                                                    "}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.Patientdetails_2 = QtWidgets.QWidget(
            self.scrollAreaWidgetContents)
        self.Patientdetails_2.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Patientdetails_2.setFont(font)
        self.Patientdetails_2.setStyleSheet("background:#4169E1;\n"
                                            "color:#ffffff;\n"
                                            "border-radius:10px\n"
                                            "")
        self.Patientdetails_2.setObjectName("Patientdetails_2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.Patientdetails_2)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.widget_25 = QtWidgets.QWidget(self.Patientdetails_2)
        self.widget_25.setObjectName("widget_25")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_25)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.widget_25)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.verticalLayout_27.addWidget(self.widget_25)
        self.widget_26 = QtWidgets.QWidget(self.Patientdetails_2)
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_26)
        self.horizontalLayout_20.setContentsMargins(9, 0, 6, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_20.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_20.addWidget(self.label_22)
        self.verticalLayout_27.addWidget(self.widget_26)
        self.widget_27 = QtWidgets.QWidget(self.Patientdetails_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget_27.setFont(font)
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_21.setContentsMargins(-1, -1, 6, 6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_38 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_21.addWidget(self.label_38)
        self.label_42 = QtWidgets.QLabel(self.widget_27)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_21.addWidget(self.label_42)
        self.verticalLayout_27.addWidget(self.widget_27)
        self.verticalLayout_26.addWidget(self.Patientdetails_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_23.addWidget(self.scrollArea)
        self.widget_6 = QtWidgets.QWidget(self.human_data)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_6.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background:#4169E1;\n"
                                        "color:#ffffff;\n"
                                        "border-radius:10px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_24.addWidget(
            self.pushButton_6, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_23.addWidget(self.widget_6)
        self.stackedWidget.addWidget(self.human_data)
        self.verticalLayout_13.addWidget(self.stackedWidget)
        self.main_screen.addWidget(self.logs_page)
        # -----------------------------------------------------------#

        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.main_screen.addWidget(self.graph_page)
        self.horizontalLayout_8.addWidget(self.main_screen)
        self.horizontalLayout.addWidget(self.stacked_pages_container)
        self.right_sidebar = QtWidgets.QWidget(self.Main_screen_container)
        self.right_sidebar.resize(1000,1000)
        ui = Ui_SideBar()
        ui.setupUi(self.right_sidebar)
        self.right_sidebar.show()
        self.horizontalLayout.addWidget(self.right_sidebar)
        self.verticalLayout.addWidget(self.Main_screen_container)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_screen.setCurrentIndex(0)
        self.ModeStackedWindow.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
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

    def showLogsScreen(self, event):
        self.main_screen.setCurrentIndex(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

       
        self.label_9.setText(_translate("MainWindow", "Baby Temperature"))
        self.label_11.setText(_translate("MainWindow", "32°C"))
        self.pushButton.setText(_translate("MainWindow", "Set Temperature"))
        self.label_41.setText(_translate("MainWindow", "Noice Level dB(A)"))
        self.manual_noice_label.setText(_translate("MainWindow", "94"))
        self.label_43.setText(_translate("MainWindow", "Light level Lux"))
        self.manual_light_label.setText(_translate("MainWindow", "100"))
        self.label_45.setText(_translate("MainWindow", "Power"))
        self.manual_power_label.setText(_translate("MainWindow", "30%"))
        self.label_28.setText(_translate("MainWindow", "Power"))
        self.label_24.setText(_translate("MainWindow", "100%"))
        self.label_27.setText(_translate("MainWindow", "Noice Level dB(A)"))
        self.label_25.setText(_translate("MainWindow", "94"))
        self.label_29.setText(_translate("MainWindow", "Light level Lux"))
        self.label_26.setText(_translate("MainWindow", "100"))
        self.label_34.setText(_translate("MainWindow", "Baby Temperature"))
        self.label_35.setText(_translate("MainWindow", "32°C"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Temperature"))
        self.label_30.setText(_translate("MainWindow", "Noice Level dB(A)"))
        self.label_31.setText(_translate("MainWindow", "94"))
        self.label_32.setText(_translate("MainWindow", "Light level Lux"))
        self.label_33.setText(_translate("MainWindow", "100"))
        self.label_36.setText(_translate("MainWindow", "Power"))
        self.label_37.setText(_translate("MainWindow", "30%"))
        self.mode_text.setText(_translate("MainWindow", "Mode"))
        self.auto_btn.setText(_translate("MainWindow", "Auto Mode"))
        self.manual_btn.setText(_translate("MainWindow", "Manual Mode"))
        self.preheat_btn.setText(_translate("MainWindow", "Preheat Mode"))
       
        self.human_data_btn.setText(_translate("MainWindow", "Human Data"))
        self.alarm_log_btn.setText(_translate("MainWindow", "Alarms log"))
        self.label_14.setText(_translate("MainWindow", "Temperature Hot"))
        self.label_15.setText(_translate("MainWindow", "Date: 12/02/2023"))
        self.label_16.setText(_translate("MainWindow", "Time: 12:21"))
        self.pushButton_5.setText(_translate(
            "MainWindow", "Export as .csv file"))
        self.label_19.setText(_translate("MainWindow", "Patient Id: 1298"))
        self.label_20.setText(_translate(
            "MainWindow", "Name: Irshit Mukherjee"))
        self.label_21.setText(_translate("MainWindow", "Weight: 5000gm"))
        self.label_22.setText(_translate("MainWindow", "Gender: Male"))
        self.label_38.setText(_translate("MainWindow", "Date: 12/02/2023"))
        self.label_42.setText(_translate("MainWindow", "Time: 12:20 pm"))
        self.pushButton_6.setText(_translate("MainWindow", "Add data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 82))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 841, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(288, 139))
        self.groupBox_3.setMaximumSize(QtCore.QSize(350, 16777215))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 421, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget_2)
        self.treeWidget.setMaximumSize(QtCore.QSize(330, 380))
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(288, 139))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 411, 371))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_2.setMaximumSize(QtCore.QSize(16777215, 380))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 510, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(870, 380, 431, 121))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 540, 431, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1200, 510, 101, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(870, 510, 321, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(870, 110, 431, 121))
        self.listWidget_3.setObjectName("listWidget_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(870, 240, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1190, 240, 111, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(870, 270, 431, 31))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(720, 510, 131, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(870, 340, 381, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(870, 70, 431, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.combo_configs = QtWidgets.QComboBox(self.centralwidget)
        self.combo_configs.setGeometry(QtCore.QRect(370, 30, 491, 31))
        self.combo_configs.setObjectName("combo_configs")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 10, 55, 16))
        self.label_4.setObjectName("label_4")
        self.send_config_to_parse_timing = QtWidgets.QPushButton(self.centralwidget)
        self.send_config_to_parse_timing.setGeometry(QtCore.QRect(550, 60, 151, 31))
        self.send_config_to_parse_timing.setObjectName("send_config_to_parse_timing")
        self.send_config_to_parse = QtWidgets.QPushButton(self.centralwidget)
        self.send_config_to_parse.setGeometry(QtCore.QRect(710, 60, 151, 31))
        self.send_config_to_parse.setObjectName("send_config_to_parse")
        self.update_list_of_configs = QtWidgets.QPushButton(self.centralwidget)
        self.update_list_of_configs.setGeometry(QtCore.QRect(740, 10, 121, 21))
        self.update_list_of_configs.setObjectName("update_list_of_configs")
        self.save_config_parse_timing = QtWidgets.QPushButton(self.centralwidget)
        self.save_config_parse_timing.setGeometry(QtCore.QRect(870, 300, 431, 31))
        self.save_config_parse_timing.setObjectName("save_config_parse_timing")
        self.save_config_parse = QtWidgets.QPushButton(self.centralwidget)
        self.save_config_parse.setGeometry(QtCore.QRect(870, 570, 431, 31))
        self.save_config_parse.setObjectName("save_config_parse")
        self.config_save_name = QtWidgets.QTextEdit(self.centralwidget)
        self.config_save_name.setGeometry(QtCore.QRect(870, 30, 431, 31))
        self.config_save_name.setObjectName("config_save_name")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(870, 10, 181, 16))
        self.label_5.setObjectName("label_5")
        self.delete_config = QtWidgets.QPushButton(self.centralwidget)
        self.delete_config.setGeometry(QtCore.QRect(370, 60, 171, 31))
        self.delete_config.setObjectName("delete_config")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1120, 340, 186, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Сайт"))
        self.pushButton.setText(_translate("MainWindow", "Обновить категории"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Категории"))
        self.pushButton_5.setText(_translate("MainWindow", ">>>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Товары"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить в разовый"))
        self.pushButton_3.setText(_translate("MainWindow", "Парсинг"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить ссылку"))
        self.pushButton_7.setText(_translate("MainWindow", "Добавить ссылку"))
        self.pushButton_4.setText(_translate("MainWindow", "Парсинг"))
        self.pushButton_8.setText(_translate("MainWindow", "Добавить в парс по t"))
        self.label_2.setText(_translate("MainWindow", "Разовый парсинг"))
        self.label_3.setText(_translate("MainWindow", "Парсинг по таймингу"))
        self.pushButton_10.setText(_translate("MainWindow", "Очистить"))
        self.label_4.setText(_translate("MainWindow", "Конфиги"))
        self.send_config_to_parse_timing.setText(_translate("MainWindow", "В парсинг по таймингу"))
        self.send_config_to_parse.setText(_translate("MainWindow", "В разовый парсинг"))
        self.update_list_of_configs.setText(_translate("MainWindow", "обновить конфиги"))
        self.save_config_parse_timing.setText(_translate("MainWindow", "Сохранить конфиг из парсинга по таймингу"))
        self.save_config_parse.setText(_translate("MainWindow", "Сохранить конфиг из разового парсинга"))
        self.label_5.setText(_translate("MainWindow", "имя сохраняемого конфига"))
        self.delete_config.setText(_translate("MainWindow", "удалить выбранный конфиг"))
        self.pushButton_9.setText(_translate("MainWindow", "Очистить"))
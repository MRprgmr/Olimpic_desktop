# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mw_icons/mw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tw = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tw.setFont(font)
        self.tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(5)
        self.tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(4, item)
        self.tw.horizontalHeader().setDefaultSectionSize(140)
        self.tw.horizontalHeader().setHighlightSections(False)
        self.tw.horizontalHeader().setStretchLastSection(True)
        self.tw.verticalHeader().setHighlightSections(True)
        self.tw.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tw)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.del_but = QtWidgets.QPushButton(self.centralwidget)
        self.del_but.setMinimumSize(QtCore.QSize(100, 40))
        self.del_but.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.del_but.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mw_icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.del_but.setIcon(icon1)
        self.del_but.setIconSize(QtCore.QSize(24, 24))
        self.del_but.setObjectName("del_but")
        self.horizontalLayout_3.addWidget(self.del_but)
        self.export_but = QtWidgets.QPushButton(self.centralwidget)
        self.export_but.setMinimumSize(QtCore.QSize(110, 40))
        self.export_but.setMaximumSize(QtCore.QSize(110, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.export_but.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mw_icons/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.export_but.setIcon(icon2)
        self.export_but.setIconSize(QtCore.QSize(24, 24))
        self.export_but.setObjectName("export_but")
        self.horizontalLayout_3.addWidget(self.export_but)
        self.clear_but = QtWidgets.QPushButton(self.centralwidget)
        self.clear_but.setMinimumSize(QtCore.QSize(120, 40))
        self.clear_but.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.clear_but.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/mw_icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clear_but.setIcon(icon3)
        self.clear_but.setIconSize(QtCore.QSize(28, 28))
        self.clear_but.setObjectName("clear_but")
        self.horizontalLayout_3.addWidget(self.clear_but)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.com_box = QtWidgets.QComboBox(self.centralwidget)
        self.com_box.setMinimumSize(QtCore.QSize(220, 30))
        self.com_box.setMaximumSize(QtCore.QSize(240, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.com_box.setFont(font)
        self.com_box.setObjectName("com_box")
        self.horizontalLayout_4.addWidget(self.com_box)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refr_lab = QtWidgets.QLabel(self.centralwidget)
        self.refr_lab.setMinimumSize(QtCore.QSize(32, 32))
        self.refr_lab.setMaximumSize(QtCore.QSize(32, 32))
        self.refr_lab.setStyleSheet("border: 1px solid rgb(180, 180, 180);\n"
"\n"
"")
        self.refr_lab.setText("")
        self.refr_lab.setScaledContents(True)
        self.refr_lab.setObjectName("refr_lab")
        self.horizontalLayout.addWidget(self.refr_lab)
        self.refr_but = QtWidgets.QPushButton(self.centralwidget)
        self.refr_but.setMinimumSize(QtCore.QSize(32, 32))
        self.refr_but.setMaximumSize(QtCore.QSize(32, 32))
        self.refr_but.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 1px solid rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"")
        self.refr_but.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/mw_icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.refr_but.setIcon(icon4)
        self.refr_but.setIconSize(QtCore.QSize(26, 26))
        self.refr_but.setObjectName("refr_but")
        self.horizontalLayout.addWidget(self.refr_but)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.set_but = QtWidgets.QPushButton(self.centralwidget)
        self.set_but.setMinimumSize(QtCore.QSize(32, 32))
        self.set_but.setMaximumSize(QtCore.QSize(32, 32))
        self.set_but.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 1px solid rgb(180, 180, 180);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"")
        self.set_but.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/mw_icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.set_but.setIcon(icon5)
        self.set_but.setIconSize(QtCore.QSize(26, 26))
        self.set_but.setObjectName("set_but")
        self.horizontalLayout_4.addWidget(self.set_but)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.cm = QtWidgets.QLabel(self.centralwidget)
        self.cm.setMinimumSize(QtCore.QSize(320, 240))
        self.cm.setMaximumSize(QtCore.QSize(320, 240))
        self.cm.setStyleSheet("border: 1px solid rgb(170, 170, 170);\n"
"border-radius: 5px;")
        self.cm.setText("")
        self.cm.setScaledContents(True)
        self.cm.setObjectName("cm")
        self.verticalLayout.addWidget(self.cm)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setMinimumSize(QtCore.QSize(80, 40))
        self.start_but.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.start_but.setFont(font)
        self.start_but.setObjectName("start_but")
        self.horizontalLayout_2.addWidget(self.start_but)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.stop_bot = QtWidgets.QPushButton(self.centralwidget)
        self.stop_bot.setMinimumSize(QtCore.QSize(80, 40))
        self.stop_bot.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.stop_bot.setFont(font)
        self.stop_bot.setObjectName("stop_bot")
        self.horizontalLayout_2.addWidget(self.stop_bot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.status_text = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.status_text.setFont(font)
        self.status_text.setObjectName("status_text")
        self.horizontalLayout_5.addWidget(self.status_text)
        self.status_info = QtWidgets.QLabel(self.centralwidget)
        self.status_info.setMinimumSize(QtCore.QSize(32, 32))
        self.status_info.setMaximumSize(QtCore.QSize(32, 32))
        self.status_info.setStyleSheet("border: 1px solid rgb(180, 180, 180);\n"
"\n"
"")
        self.status_info.setText("")
        self.status_info.setScaledContents(True)
        self.status_info.setObjectName("status_info")
        self.horizontalLayout_5.addWidget(self.status_info)
        self.status_info_icon = QtWidgets.QPushButton(self.centralwidget)
        self.status_info_icon.setMinimumSize(QtCore.QSize(32, 32))
        self.status_info_icon.setMaximumSize(QtCore.QSize(32, 32))
        self.status_info_icon.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 1px solid rgb(180, 180, 180);\n"
"}\n"
"")
        self.status_info_icon.setText("")
        self.status_info_icon.setIconSize(QtCore.QSize(26, 26))
        self.status_info_icon.setObjectName("status_info_icon")
        self.horizontalLayout_5.addWidget(self.status_info_icon)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/mw_icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Olimpiad Registration"))
        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First name"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last name"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Class"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone number"))
        self.del_but.setText(_translate("MainWindow", "Delete"))
        self.export_but.setText(_translate("MainWindow", "Export as"))
        self.clear_but.setText(_translate("MainWindow", "Clear all"))
        self.label.setText(_translate("MainWindow", "Total:          0"))
        self.start_but.setText(_translate("MainWindow", "Start"))
        self.stop_bot.setText(_translate("MainWindow", "Stop"))
        self.status_text.setText(_translate("MainWindow", "Tekshirilmoqda"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

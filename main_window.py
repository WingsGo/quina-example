# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Jun 10 13:59:08 2018
#      by: pyside2-uic  running on PySide2 5.9.0a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = Widget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # add this call to set central widget
        MainWindow.set_central_widget(self.centralwidget)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = GroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = Label(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = LineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = Label(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = LineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = Label(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = LineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = PushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = PushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = GroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = Label(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = LineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = Label(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_5 = LineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = Label(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_6 = LineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_3 = PushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_4 = PushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))


from quina.widgets import Label, Widget, PushButton, LineEdit, GroupBox

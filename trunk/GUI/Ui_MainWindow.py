# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ssorgatem/Documents/python/video4fuze/GUI/MainWindow.ui'
#
# Created: Mon Aug 17 03:03:35 2009
#      by: PyQt4 UI code generator 4.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 418)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 501, 281))
        self.tableWidget.setMinimumSize(QtCore.QSize(501, 281))
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.RemoveButton = QtGui.QPushButton(self.centralWidget)
        self.RemoveButton.setGeometry(QtCore.QRect(400, 29, 131, 25))
        self.RemoveButton.setMinimumSize(QtCore.QSize(131, 25))
        self.RemoveButton.setObjectName("RemoveButton")
        self.ConvertButton = QtGui.QPushButton(self.centralWidget)
        self.ConvertButton.setGeometry(QtCore.QRect(220, 350, 131, 25))
        self.ConvertButton.setMinimumSize(QtCore.QSize(131, 25))
        self.ConvertButton.setObjectName("ConvertButton")
        self.AddButton = QtGui.QPushButton(self.centralWidget)
        self.AddButton.setGeometry(QtCore.QRect(50, 30, 131, 25))
        self.AddButton.setMinimumSize(QtCore.QSize(131, 25))
        self.AddButton.setObjectName("AddButton")
        self.SelectOutputButton = QtGui.QPushButton(self.centralWidget)
        self.SelectOutputButton.setGeometry(QtCore.QRect(210, 30, 161, 25))
        self.SelectOutputButton.setMinimumSize(QtCore.QSize(131, 25))
        self.SelectOutputButton.setObjectName("SelectOutputButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 582, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAdd_file = QtGui.QAction(MainWindow)
        self.actionAdd_file.setObjectName("actionAdd_file")
        self.actionAbout_video4fuze = QtGui.QAction(MainWindow)
        self.actionAbout_video4fuze.setObjectName("actionAbout_video4fuze")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionRemove_selected_files = QtGui.QAction(MainWindow)
        self.actionRemove_selected_files.setObjectName("actionRemove_selected_files")
        self.actionSelect_output_folder = QtGui.QAction(MainWindow)
        self.actionSelect_output_folder.setObjectName("actionSelect_output_folder")
        self.menuFile.addAction(self.actionAdd_file)
        self.menuFile.addAction(self.actionRemove_selected_files)
        self.menuFile.addAction(self.actionSelect_output_folder)
        self.menuHelp.addAction(self.actionAbout_video4fuze)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableWidget, self.RemoveButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "video4fuze", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.RemoveButton.setText(QtGui.QApplication.translate("MainWindow", "Remove files", None, QtGui.QApplication.UnicodeUTF8))
        self.ConvertButton.setText(QtGui.QApplication.translate("MainWindow", "Convert!", None, QtGui.QApplication.UnicodeUTF8))
        self.AddButton.setText(QtGui.QApplication.translate("MainWindow", "Add files...", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectOutputButton.setText(QtGui.QApplication.translate("MainWindow", "Select output folder", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_file.setText(QtGui.QApplication.translate("MainWindow", "Add files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_video4fuze.setText(QtGui.QApplication.translate("MainWindow", "About video4fuze", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_selected_files.setText(QtGui.QApplication.translate("MainWindow", "Remove selected files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_output_folder.setText(QtGui.QApplication.translate("MainWindow", "Select output folder", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


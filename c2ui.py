# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c1post.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 781, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(180, 70, 121, 41))
        self.pushButton.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 150, 121, 31))
        self.pushButton_2.setStyleSheet("font: 9pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        #
        self.lineEdit = NewQLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(180, 240, 291, 31))
        self.lineEdit.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(180, 140, 291, 71))
        self.textEdit.setStyleSheet("font: 75 9pt \"微软雅黑\";\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 310, 291, 71))
        self.textEdit_2.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 250, 121, 41))
        self.pushButton_3.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.pushButton_3.setObjectName("pushButton_3")
        #
        self.lineEdit_2 = NewQLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 40, 281, 71))
        self.lineEdit_2.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        #
        self.lineEdit_3 = NewQLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 270, 281, 71))
        self.lineEdit_3.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        #
        self.lineEdit_4 = NewQLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 150, 281, 71))
        self.lineEdit_4.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 120, 121, 41))
        self.pushButton_4.setStyleSheet("font: 75 9pt \"微软雅黑\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 641, 391))
        self.label.setStyleSheet("font: 75 24pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(MainWindow.openfile)
        self.pushButton_2.clicked.connect(MainWindow.post)
        self.pushButton_4.clicked.connect(MainWindow.start_test)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_2.setText(_translate("MainWindow", "post"))
        self.lineEdit.setText(_translate("MainWindow", "文件拖拽到此处"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">文件名选择</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">发送状态</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "服务器发送"))
        self.pushButton_3.setText(_translate("MainWindow", "Plot"))
        self.lineEdit_2.setText(_translate("MainWindow", "adb工具位置拖拽到此处"))
        self.lineEdit_3.setText(_translate("MainWindow", "数据集位置拖拽到此处"))
        self.lineEdit_4.setText(_translate("MainWindow", "模型位置拖拽到此处"))
        self.pushButton_4.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Simplify测试启动"))
        self.label.setText(_translate("MainWindow", "结果图显示位置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "结果图"))

#拖拽方法实现
# 该块儿仅为框架，不可直接拿走使用
# 以下为重写的方法
class NewQLineEdit(QtWidgets.QLineEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 删除没有影响，目前不确定（因为True和False测试结果一样）
        self.setDragEnabled(True)  # 删除没有影响，（因为True和False测试结果一样）

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入文件


    def dropEvent(self, event):    # 本方法为父类方法，本方法中的event为鼠标放事件对象
        urls = [u for u in event.mimeData().urls()]  # 范围文件路径的Qt内部类型对象列表，由于支持多个文件同时拖入所以使用列表存放
        for url in urls:
            self.setText(url.path()[1:])# 将Qt内部类型转换为字符串类型
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

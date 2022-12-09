from c2ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog  # 导入qt窗体类

import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import sys

from adb import *

import requests

class main(Ui_MainWindow,QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        #super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def post1(self,filepath):
        try:
            url = 'http://127.0.0.1:5000'
            str000 = filepath
            newname = str000.split('/')
            print(newname[len(newname) - 1])
            newname1 = str(newname[len(newname) - 1])

            # 传单张图片
            # files = {'file':(newname1,open(r'C:\Users\komorip\Desktop\daliy\python\wrb\server\post\2.jpg','rb'),'image/jpg')}

            files = {'file': (
                newname1, open(filepath, 'rb'),
                'application/x-zip-compressed')}
            r = requests.post(url, files=files)
            result = newname1 + '\n' + r.text
            return result
        except:
            ####
            self.lineEdit.setText("1")
            error_dialog = QtWidgets.QErrorMessage()

            error_dialog.showMessage('''Oh no!错误位置：// post1 //函数 出现问题，请检查一下您的url设置或者也有可能出现其他问题!
            ┭┮﹏┭┮''')

            error_dialog.exec()

    def tplot(self,x_data, y_data):
        # 正确显示中文和负号
        try:
            plt.rcParams["font.sans-serif"] = ["SimHei"]
            plt.rcParams["axes.unicode_minus"] = False

            # 画图，plt.bar()可以画柱状图
            for i in range(len(x_data)):
                plt.bar(x_data[i], y_data[i])
            # 设置图片名称
            plt.title("销量分析")
            # 设置x轴标签名
            plt.xlabel("年份")
            # 设置y轴标签名
            plt.ylabel("销量")
            # 显示  自动覆盖生成新图
            savefig(r".\ui\tpolt\1.jpg")
            return 1
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('''Oh no!错误位置：// tplot //函数出现问题\n，请检查一下函数输入的数据对是否匹配，或者存在其他错误!
                                                                  ┭┮﹏┭┮''')
            error_dialog.exec()

            return 0


    def openfile(self):
        try:
            global filep
            # 打开文件的窗体，进行图片的选择
            openfile_name = QFileDialog.getOpenFileName()
            if openfile_name[0] != '':

            #格式测试
                print(openfile_name[0])

                filep = openfile_name[0]   # 获取选中的图片路径
                self.textEdit.setText(filep)
        except:
            pass
    def post(self):
        try:
            global filep
            #要调用才能选中文件地址
            self.drag_addrss()


            result=self.post1(filep)



            self.textEdit_2.setText(result)
        except:
           pass

    def readQss(style):
        try:
            with open(style, 'r') as f:
                return f.read()
        except:
            pass

    def drag_addrss(self):
        try:
             global filep
             filep=self.lineEdit.text()
             # test
             self.textEdit.setText(filep)
        except:
            pass


    def utplot(self,x_data , y_data ):
        # 正确显示中文和负号
        try:

            x=self.tplot(x_data , y_data)
            if x==1:
                self.label.setPixmap(QtGui.QPixmap(r".\ui\tpolt\1.jpg"))
                self.label.setScaledContents(True)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('''Oh no!错误位置: // utplot //函数出现问题 ，\n请检查一下!
                    ┭┮﹏┭┮''')
    #按钮绑定

    def start_test(self):
        try:
            #adb=self.lineEdit_2.text()
          #  cadb_path(adb)
            model=self.lineEdit_4.text()
            dataset=self.lineEdit_3.text()
            start_main_activity(dataset_path=dataset,model_path=model)
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('''Oh no!错误位置: // start_test //函数出现问题 ，\n请检查一下!
                                ┭┮﹏┭┮''')
            error_dialog.exec()

if __name__=="__main__":
    app = QApplication(sys.argv)

    styleFile = r".\ui\QSS-master\ElegantDark.qss"



    ui=main()

    style = main.readQss(styleFile)
    ui.setStyleSheet(style)

    ui.show()

    #ui.pushButton.clicked.connect(ui.openfile)
    #ui.pushButton_2.clicked.connect(ui.post)

    # test

    a = ["wo", "oo", "2h", "3", "4", "8"]
    b = [20, 70, 40, 62, 45, 70]

    ui.pushButton_3.clicked.connect(lambda: ui.utplot(a, b))
    sys.exit(app.exec_())
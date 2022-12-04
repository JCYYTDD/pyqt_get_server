import requests
from PyQt5 import QtCore, QtGui, QtWidgets
def post1(filepath):
    try:
        url = 'http://127.0.0.1:5000'
        str000=filepath
        newname = str000.split('/')
        print(newname[len(newname)-1])
        newname1=str(newname[len(newname)-1])



        #传单张图片
        #files = {'file':(newname1,open(r'C:\Users\komorip\Desktop\daliy\python\wrb\server\post\2.jpg','rb'),'image/jpg')}

        files = {'file': (
            newname1, open(filepath, 'rb'),
            'application/x-zip-compressed')}
        r = requests.post(url,files=files)
        result = newname1+'\n'+r.text
        return result
    except:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('''Oh no!post函数出现问题，请检查一下您的url配置或者也有可能出现其他问题!
        ┭┮﹏┭┮''')


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

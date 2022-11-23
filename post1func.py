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

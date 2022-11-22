import requests
def post1(filepath):
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

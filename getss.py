import requests

def getweb(a):
    r = requests.get(url=a)
    #print(r.status_code)
   # print(r.url)
    #print(r.text)
    return r.text






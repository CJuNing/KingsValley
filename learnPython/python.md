# respone 用法

``` python
    respones.status_code "状态码"
    200

    r.encoding = 'utf-8'
    r.text

    r.content
```

# pyinstaller 安装错误 解决办法

```
1.其实一点也不麻烦
2.先“pip install pywin32”
3.在“pip install wheel”
4.试一下“pip install pyinstaller”

```


pyinstaller -F --icon=1234.ico run.py -w

pyinstaller -p site-packages --icon=1.ico -F doit.py -w

pyinstaller -p site-packages --icon=1.ico -F doit.py --noconsole

pyinstaller -p site-packages --icon=1.ico -F doit.py -w

 打包安装遇到的问题分享：
1.在进行打包的时候遇到报错：

?
1
2
Fatal error: PyInstaller does not include a pre-compiled bootloader for your
platform.<a href="https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html">https://pyinstaller.readthedocs.io/en/stable/bootloader-building.html</a>
查阅资料后发现可以通过降级实现，后来我发现造成这个问题主要是后台的win10防火墙吧我虚拟环境中的pyinstaller的pyinstaller\PyInstaller\bootloader\Windows-32bit中的runw.exe删掉了，可以通过原有python库中已有的库中去复制粘贴到相应的路径下，防火墙应该时删掉了某些重要的东西。

但是我发现后来打包中一旦带有

2.打包后发现的一些问题：numpy： No module named ‘numpy.random common'

可以发现使用numpy下，pandas的下引用的numpy导入失败，经查阅这可能是版本问题造成的

可以先卸载原有的版本pip uninstall numpy

改为安装pip install numpy==1.16.2

 3.distutils not included with latest virtualenv (16.4.0) #4064

打包出来可能会发现缺少导入包distutils，因为distutils是内置库，无法pip install 安装，并且virtualenv16.4以后就不再自带库distutils库了。

所以可以通过降低virtualenv解决这个问题；
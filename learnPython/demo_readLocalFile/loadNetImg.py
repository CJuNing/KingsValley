
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入模块
import requests
 
# 现在可以调用模块里包含的函数了
r = requests.get('https://avatar.csdn.net/2/E/C/3_u010590983.jpg')
with open('./output/avatar.jpg','wb') as f:
    f.write(r.content)
import requests

baseUrl = "http://localhost:8100"
url = baseUrl + "/save"
files = {'img': ('1.png', open('./input/1.png', 'rb'), 'image/png', {})}
res=requests.request("POST",url, data=None, files=files)



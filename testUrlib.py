from urllib import response
import urllib.request
import urllib.parse



#获取post请求， 模拟用户灯火从而获取数据

data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
x = urllib.request.urlopen("http://httpbin.org/post", data=data)

print(x.read().decode("utf-8"))


#超时处理

try:
    a = urllib.request.urlopen("http://httpbin.org/get" ,timeout=0.01)
    print(a.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")



#基础解码网页内容
x = urllib.request.urlopen("http://baidu.com")
print(x.getheader("Server"))



#伪装成浏览器
url = ""
data =bytes(urllib.parse.urlencode({'name':'y'}),encoding="utf-8")
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}
req = urllib.request.Request(url=url, data=data,headers=headers,method="POST")


#访问豆瓣封装
url = "https://www.douban.com"
data =bytes(urllib.parse.urlencode({'name':'y'}),encoding="utf-8")
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}
req = urllib.request.Request(url=url,headers=headers)
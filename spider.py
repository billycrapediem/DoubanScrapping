# -*- coding = utf-8 -*-
import code
from turtle import title
from urllib import response
from wsgiref.util import request_uri
from bs4 import BeautifulSoup       ##网页解析，获取数据指定
import re      ## 正则表达式，进行文字匹配
import urllib.request, urllib.error  ## 指定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行sqlite数据库操作


def main():    # 1.爬取网页 2.逐一解析数据 3.保存数据

    baserurl = "https://movie.douban.com/top250?start="
    datalist =  getData(baserurl)
    savepath = r".\\豆瓣电影top250.xls"
    #3. 保存数据
#    saveData(savepath)


findLink = re.compile(r'<a href="(.*)">')
findTitle = re.compile(r'<span class="title">(.*)</span>')
findImgSrc = re.compile(r'<img.*src="(.*?)" width="100"/>',re.S) # 后面re.S表示忽略换行符
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


def getData(baseurl): #爬取网页
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)          #保存获取到的页码

        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser") # 使用html解析器
        for item in soup.find_all('div',class_="item"): #查抄符合要求的字符串，形成列表
            data =[] #一部电影的全部信息
            item = str(item)
            link = re.findall(findLink,item)[0]  #re库迎来通过正则表达式查找指定的字符串
            data.append(link)
            titles = re.findall(findTitle,item) 
            if len(titles) == 2 :
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else : 
                data.append(titles[0])
                data.append(' ')
            img = re.findall(findImgSrc,item)[0] #去掉无关的符号
            data.append(img)
            rating = re.findall(findRating,item)[0] 
            data.append(rating)
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else: 
                data.append(" ")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?>(\s+)'," ",bd)
            bd = re.sub('/'," ",bd)
            data.append(bd.strip()) #去掉前后的空格
            #把处理好的电影信息放进datalist 
            datalist.append(data)
    
    # 解析数据
    return datalist


#得到制定一个url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    } #用户代理表示告诉豆瓣服务器，我们是什么类型的机器，(告诉浏览器我们可以接受什么水平的文件)
    request = urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:      #报错输出
        if hasattr(e,"code"):
            print(e,code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html 

def saveData(savepath):
    print("hello")




if __name__ == "__main__":
    main()

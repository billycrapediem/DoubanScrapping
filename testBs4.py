#beautifulsoup4 是将html文档转换为树形结构
# Tag
# NavigableString
#BeautifulSoup
#Comment

from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")


print(bs.title)
print(bs.a)
# 1.tag 标签及其内容，拿到他所找到的第一个内容

print(type((bs.title.string)))
# 2.navigatablestring 标签里面的内容

print(bs.a.attrs)

print(bs)


# 文档的遍历 把文档信息按照list形式放进元素

bs.contents
bs.children



#文档的搜索

#(1) find_all()
#字符串过滤：会找到与字符串完全匹配的内容
t_list = bs.find_all("a")

# 表达式搜索：使用search()方法匹配内容

t_list = bs.find_all(re.compile("a"))

#方法： 传入一个函数，根据函数的要求搜索


def name_is_exist(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exist)

print(t_list)


#(2) kwargs 参数
t_list  = bs.find_all(id="head")
t_list = bs.find_all(href="http://news.baidu.com")

for item in t_list:
    print(item)

#3.text参数

t_list = bs.find_all(text = "hao123")
t_list = bs.find_all(text = ["hao123","地图"])

#4. limit 参数

t_list = bs.find_all("a",limit=3)

#css选择器

t_list = bs.select('title') #通过标签来查找
t_list = bs.select(".mnav") #通过类名来查找
t_list = bs.select("#u1") #t通过id查找
t_list = bs.select("a[class='bri']") #通过属性查找
t_list = bs.select("head>title") #通过子标签查找

#同级查找

t_list = bs.select(".mnav ~ .bri")


#正则表达式

print(re.findall("[A-Z]","ASDsfsdf")) # 前面字符串是正则表达式，后面字符串是被校验的对象

#sub 
print(re.sub("a","A","abcdcasd")) #第一个字符窜是被替换的对象，第二个字符窜是替换对象，在第三个字符串中查找



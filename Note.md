###需求
* 获取豆瓣TOP250电影相关信息
* https://movie.douban.com/top250

###准备工作
* url 分析
    * 每个页面的url规律， 最后的页面数值等于页数减
    * headers response F12，开发者平台 cookie 以及 user-response操作

###编码规范
* pthon程序第一行加入 # -*-conding: utf-8 -
* python 文件可以加入main函数用于测试程序

###引入模块
* 
``` python
import sys 
import bs4 
import re
import urllib.request, urllib.error
import xlwt
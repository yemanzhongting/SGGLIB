# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import json
import jsonpath
star_url="http://www.12379.cn/data/alarm_list_all.html"
#G:\ProgramData\Anaconda3\phantomjs-2.1.1-windows\bin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
douban='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=60&limit=20'
header={
    'Host':'movie.douban.com',
     'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',


}
def get_channel_urls(url):
    wb_data=requests.get(url,headers=header)
    soup=json.loads(wb_data.text)
    qq = jsonpath.jsonpath(soup[0])#'$..actor'
    for i in qq:
        print(i)
    #print(soup['actors'])

    ##idData1 > tbody > tr:nth-child(1) > td:nth-child(1) > a
    ##idData1 > tbody > tr:nth-child(1) > td:nth-child(1) > a
if __name__ == "__main__":

    get_channel_urls(douban)
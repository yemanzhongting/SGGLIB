from bs4 import BeautifulSoup
import requests

start_url="https://bj.58.com/sale.shtml"

def get_channel_urls(url):
    wb_data=requests.get(start_url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    
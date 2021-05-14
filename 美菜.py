import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
aa=[]
bb=[]
cc=[]
dd=[]
i=1
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
url='https://online.yunshanmeicai.com/entry/index#/mall'

r=requests.get(url,headers=headers)
r.encoding='UTF-8'
soup=BeautifulSoup(r.text,'lxml')
name=soup.findAll("div",{"class":"sku-title"})
price=soup.findAll("div",{"class":"price sale-info"})
# link=soup.findAll("li",{"class":"col-xs-6"})
print(name)
time.sleep(1)
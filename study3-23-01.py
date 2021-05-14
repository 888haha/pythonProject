import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import numpy as np
import time
dd=[]
aa=[]
bb=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE"}
url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=&pvid=11cf57413ef44a7f9c70fd79ffef7964'
r=requests.get(url,headers=headers)
r.encoding='UTF-8'

soup=BeautifulSoup(r.text,'lxml')
name=soup.findAll("div",{"class":"p-name p-name-type-2"})
price=soup.findAll("div",{"class":"p-price"})
url1=soup.findAll("a",{"class":"curr-shop hd-shopname"})
for n,p,u in zip(name,price,url1):
    aa.append(n.get_text())
    bb.append(p.get_text())
    dd.append(u.get("href"))
output=pd.DataFrame({"名称":aa,"价格":bb,"网址":dd})
df=pd.DataFrame(output)
# df.to_excel('京东手机1.xlsx')
time.sleep(1)
print(output)


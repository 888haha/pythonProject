import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import numpy as np
import time

aa=[]
bb=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE"}
url='http://m.zhuanzhuan.com/youpin/website/list.html?source=wuba&filter=pve_5461_101_pve_5462_2101018&from=old_yp_jg_maishouji'
r=requests.get(url,headers=headers)
r.encoding='UTF-8'
soup=BeautifulSoup(r.text,'lxml')

name=soup.findAll("div",{"class":"title"})
price=soup.findAll("div",{"class":"price"})
# url1=soup.findAll("a",{"class":"curr-shop hd-shopname"})
for n,p in zip(name,price):
    aa.append(n.get_text())
    bb.append(p.get_text())
    # dd.append(u.get("href"))
output=pd.DataFrame({"名称":aa,"价格":bb})
df=pd.DataFrame(output)
# df.to_excel('京东手机1.xlsx')
time.sleep(1)
print(df)
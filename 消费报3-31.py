import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import numpy as np
import time
dd=[]
aa=[]
bb=[]
i=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE"}
url='http://www.315tech.com/web/complaintlist/1/'
time.sleep(1)
for i in range(0,8):
    n=str(i)
    url1=url+n
    r=requests.get(url1,headers=headers)
    soup=BeautifulSoup(r.text,'lxml')
    name=soup.findAll("div",{"class":"media-body"})
    na = soup.findAll("div", {"class": "media-body"})
    for n,n1 in zip(name,na):
        aa.append(n.get_text())
        bb.append(n1.get('href'))
output=pd.DataFrame({"标题":aa,"名称":bb})
df=pd.DataFrame(output)
# df.to_excel("tousut.xlsx")
print(df)
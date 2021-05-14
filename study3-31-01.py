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
url='https://www.315xft.cn/news/lighthouse?pageIndex='
time.sleep(1)
for i in range(1,11):
    n=str(i)
    url1=url+n
    # print(url1)
    r=requests.get(url1,headers=headers)
    r.encoding='UTF-8'
    soup=BeautifulSoup(r.text,'lxml')
    name=soup.findAll("div",{"class":"left"})
    name1=soup.findAll("td",{"class":"field2"})
    for n,na in zip(name,name1):
        aa.append(n.get_text())
        bb.append(na.get_text())
output=pd.DataFrame({"名称":aa,"链接":bb})
df=pd.DataFrame(output)
# df.to_excel("投诉.xlsx")

print(output)
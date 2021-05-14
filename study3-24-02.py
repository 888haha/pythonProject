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
url='https://tousu.sina.com.cn/'
r=requests.get(url,headers=headers)
r.encoding='UTF-8'
soup=BeautifulSoup(r.text,'lxml')
name=soup.findAll("div",{"class":"blackcat-con"})
name1=soup.findAll("div",{"class":"hot_blk"})
for n,na in zip(name,name1):
    aa.append(n.get_text())
    bb.append(na.get_text())
output=pd.DataFrame({"名称":aa,"链接":bb})

time.sleep(1)
print(output)
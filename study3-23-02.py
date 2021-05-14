import requests
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
import time
import pymysql
a=[]
b=[]
c=[]
d=[]
i=1
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE"}
url='http://item.pinhui001.com/site/list.html?action=1,0,0,0,0,0,0,0,0,0,0&page='
for i in range(1,14):
    url1=url+str(i)
    # print(url1)
    r=requests.get(url1,headers=headers)
    r.encoding='UTF-8'
    soup=BeautifulSoup(r.text,'lxml')
    name=soup.findAll("a",{"class":"block text-overflow-two hover"})
    price=soup.findAll("span",{"class":"c-red text-bold"})
    link=soup.findAll("a",{"class":"block text-overflow-two hover"})
    shop=soup.findAll("div",{"class":"pro-list-shop"})
    for n,p,l,s in zip(name,price,link,shop):
        a.append(n.get_text())
        b.append(p.get_text())
        c.append(l.get("href"))
        d.append(s.get_text())
output=pd.DataFrame({"名称":a,"价格":b,"链接":c,"店铺":d})
df=pd.DataFrame(output)
time.sleep(1)
print(df)
df.to_excel("中创国际.xlsx")
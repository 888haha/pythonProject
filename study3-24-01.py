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
url='https://search.jd.com/Search?keyword=%E9%B1%BC%E6%B2%B9%E8%BD%AF%E8%83%B6%E5%9B%8A&enc=utf-8&suggest=1.def.0.base&wq=%E9%B1%BC%E6%B2%B9&pvid=3c7315ebe1ce49bfbb322f8badaf5f1e'
r=requests.get(url,headers=headers)
r.encoding='UTF-8'
soup=BeautifulSoup(r.text,'lxml')
name=soup.findAll("div",{"class":"p-name p-name-type-2"})
link=soup.findAll("div",{"class":"gl-i-wrap"})
for i in link:
    li=i.find("div",{"class":"p-name p-name-type-2"}).a["href"]
    print(li)
    # df=np.array(li)
    # df=pd.DataFrame(links)
    print(li)
    # df.to_excel("京东3.xlsx")
    # print(links)
# for n,l in zip(name,link):
#     aa.append(n.get_text())
#     bb.append(l.get("href"))
#
# output=pd.DataFrame({"名称":aa,"链接":bb})
# print(output)
# # df=pd.DataFrame(output)
# # df.to_excel('京东.xlsx')

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
url='https://s.1688.com/company/company_search.htm?keywords=%B5%E7%D4%B4%CA%CA%C5%E4%C6%F7&button_click=top&n=y&netType=1%2C11%2C16&filt=y&province=%E5%B9%BF%E4%B8%9C&city=%E6%B7%B1%E5%9C%B3&beginPage=1#sm-filtbar'
# for i in range(1,14):
#     url1=url+str(i)
#     # print(url1)
r=requests.get(url,headers=headers)
r.encoding='utf8'
soup=BeautifulSoup(r.text,'lxml')
name=soup.findAll("div",{"class":"title-container"})
price=soup.findAll("div",{"class":"major-craft-box"})
print(r)

# for n,p in zip(name,price):
#     a.append(n.get_text())
#     b.append(p.get_text())
# output=pd.DataFrame({"企业":a,"主营":b})
# df=pd.DataFrame(output)
# time.sleep(2)
# print(df)
# df.to_excel("阿里茅台.xlsx")
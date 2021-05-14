import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import pymysql
from sqlalchemy import create_engine
aa=[]
bb=[]
cc=[]
dd=[]
i=1
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
url1='https://wx.gy19.com/WapShop/ProductList?keyWord=%u9152&page='
for i in range(1,29):
    url=url1+str(i)+"&size=20"
    r=requests.get(url,headers=headers)
    r.encoding='UTF-8'
    soup=BeautifulSoup(r.text,'lxml')
    name=soup.findAll("div",{"class":"name bcolor"})
    price=soup.findAll("div",{"class":"price font-s text-danger"})
    link=soup.findAll("li",{"class":"col-xs-6"})
    # print("https://wx.gy19.com/WapShop/"+lin)
    #
    for na,pr in zip(name,price):
        aa.append(na.get_text())
        bb.append(pr.get_text())
    for li in link:
        lin = li.find("div", {"class": "info"}).a["href"]
        dd=cc.append(str("https://wx.gy19.com/WapShop/" + lin))
        # print(cc)
df=pd.DataFrame({"name":aa,"price":bb,"url":cc})
# df.to_excel('data_baijiu.xlsx')


time.sleep(1)
# # data=pd.read_excel('C:/Users/hejp/PycharmProjects/pythonProject/中创国际.xlsx')
engine=create_engine('mysql+pymysql://root:739913a@localhost:3306/haha?charset=utf8')
df.to_sql('data_baijiu',con=engine,if_exists='append', index='xuhao')












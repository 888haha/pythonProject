import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import numpy as np
import time
import pymysql
from sqlalchemy import create_engine
import html
aa=[]
bb=[]
cc=[]
i=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360EE"}
# url='http://icp.chinaz.com/baidu.com'
url='http://www.air-level.com/rank'
r=requests.get(url,headers=headers)
r.encoding='gb2312'
# soup=BeautifulSoup(r.text,'lxml')
# table=pd.read_html(url)
# print(table)
df=pd.DataFrame()
for i in range(1,35):
   url='http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jjzc/index.phtml?symbol=%D6%A4%C8%AF%BC%F2%B3%C6%BB%F2%B4%FA%C2%EB&reportdate=2021&quarter=1&p='
   # url='http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList'
   # a=['QME7Bsef4_QfYYR0']
   # url1=url+str(a)+'/FundStock_Service.getFundBigholdList?page=1&num=40&sort=fHolderNum&asc=0&companyCode=&year=2020&quarter=4&type2=&type3=&symbol='
   df=pd.concat([df,pd.read_html(url+str(i))[0]])
   # df=pd.read_html(url1)
   engine=create_engine('mysql+pymysql://root:739913a@localhost:3306/haha?charset=utf8')
   # conn=pymysql.connect(host='localhost',user='root',password='739913a',)

   time.sleep(1)
   # print(df)
# df.to_excel('jijincg2021jidu1.xlsx',index='xuhao')
df.to_sql('基金重仓股2021年一季度',con=engine,if_exists='append',index='xuhao')
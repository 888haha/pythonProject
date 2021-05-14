import requests
import numpy as np
import time
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib  import pyplot as plt
import sklearn
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="739913a",db="haha")
cursor=conn.cursor()
# sql='update data_baijiu set price=88'
# sql='select 所属分局,count(*)as 线索数 from 2019年案件线索  group by 所属分局'
sql='select * from anzuos'
getdata=pd.read_sql(sql,conn)
# try:
#     cursor.execute(sql)
#     conn.commit()
# except:
#     conn.rollback()
# conn.close()
df=getdata.pivot_table(index='市场名称',values='评分',aggfunc='sum')

# print(df)
x=np.array(df.values)
y=np.array(df.index)

plt.bar(x,y)
plt.show()

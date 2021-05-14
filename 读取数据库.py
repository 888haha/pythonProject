import requests
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup
import time
import pymysql

conn=pymysql.connect(host="localhost",user="root",password="739913a",db="haha")
sql="SELECT a.所属分局,2018线索数,2019线索数 FROM(SELECT 所属分局,COUNT(线索编号) AS 2018线索数  FROM  2018年案件线索 GROUP BY 所属分局  ORDER BY 2018线索数 DESC)AS a " \
    "LEFT JOIN(SELECT 所属分局,COUNT(线索编号)AS 2019线索数  FROM  2019年案件线索 GROUP BY 所属分局 )AS b " \
    "ON a.所属分局=b.所属分局;"

getdata=pd.read_sql(sql,conn)
print(getdata)
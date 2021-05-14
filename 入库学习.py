import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import pymysql

from sqlalchemy import create_engine
data=pd.read_excel('C:/Users/hejp/PycharmProjects/pythonProject/中创国际.xlsx')
engine=create_engine('mysql+pymysql://root:739913a@localhost:3306/haha?charset=utf8')
data.to_sql('home',con=engine,if_exists='append', index=False)
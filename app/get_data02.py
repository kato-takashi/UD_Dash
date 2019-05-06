from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

df = pd.read_csv('assets/data.csv')

#型変換
date = datetime.datetime.strptime(df['date'][0],'%Y/%m/%d').date()

dates = []
for _date in df['date']:
    date = datetime.datetime.strptime(_date,'%Y/%m/%d').date()
    dates.append(date)

#受講生とreviewsの数
n_subscribers = df['subscribers'].values
n_reviews = df['reviews'].values

#前日との数の差分
diff_subscribers = df['subscribers'].diff().values
diff_reviews = df['reviews'].diff().values
print(diff_reviews)

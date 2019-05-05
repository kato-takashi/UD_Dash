from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

# url = 'https://scraping-for-beginner.herokuapp.com/udemy'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
#
# name = soup.select('.card-title')[0].string
# #「受講生の数：3534」を取得->，splitで分割->，整数化
# n_subscribers = soup.select('.subscribers')[0].string
# n_subscribers = int(n_subscribers.split('：')[1])
#
# #「レビューの数：3534」を取得->，splitで分割->，整数化
# n_reviews = soup.select('.reviews')[0].string
# n_reviews = int(n_reviews.split('：')[1])
#
# results = {
#     'name': name,
#     'n_subscribers':n_subscribers,
#     'n_reviews':n_reviews
#
# }
# #csvデータの読み込み
# df = pd.read_csv('assets/data.csv')
# date = datetime.datetime.today().strftime('%Y/%-m/%-d')
#
# subscribers = results['n_subscribers']
# reviews = results['n_reviews']
#
# #スクレイピングの結果
# scraping_result = pd.DataFrame([[date, subscribers, reviews]], columns=['date','subscribers','reviews'])
# #最新のスクレイピングの結果をcsvデータに結合
# scraping_df = pd.concat([df, scraping_result])
# df.to_csv('assets/data.csv', index=False)
# print(scraping_df.tail())

#関数化
results ={}
#urlから取得関数
def get_udemy_info():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = soup.select('.card-title')[0].string
    #「受講生の数：3534」を取得->，splitで分割->，整数化
    n_subscribers = soup.select('.subscribers')[0].string
    n_subscribers = int(n_subscribers.split('：')[1])

    #「レビューの数：3534」を取得->，splitで分割->，整数化
    n_reviews = soup.select('.reviews')[0].string
    n_reviews = int(n_reviews.split('：')[1])

    results = {
        'name': name,
        'n_subscribers':n_subscribers,
        'n_reviews':n_reviews

    }
    return results

#CSV読み込み
#csvデータの読み込み
def write_data():
    df = pd.read_csv('assets/data.csv')
    _result = get_udemy_info()

    #書き込むデータ
    date = datetime.datetime.today().strftime('%Y/%-m/%-d')
    subscribers = _result['n_subscribers']
    reviews = _result['n_reviews']

    #スクレイピングの結果
    scraping_result = pd.DataFrame([[date, subscribers, reviews]], columns=['date','subscribers','reviews'])
    print(scraping_result)
    #最新のスクレイピングの結果をcsvデータに結合
    scraping_df = pd.concat([df, scraping_result])
    df.to_csv('assets/data3.csv', index=False)
    print(scraping_df.tail())


write_data()

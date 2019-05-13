from bs4 import BeautifulSoup
import requests
from assets.database import db_session
from assets.models import Data

import datetime

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
    _result = get_udemy_info()

    #書き込むデータ
    date = datetime.date.today()
    subscribers = _result['n_subscribers']
    reviews = _result['n_reviews']

    #sql3
    row = Data(date=tate, subscribers=subscribers, reviews=reviews)
    db_session.add(row)
    db_session.commit()
    # print(scraping_df.tail())

if __name__ == '__main__':
    write_data()

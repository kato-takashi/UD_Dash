from bs4 import BeautifulSoup
import requests
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
print(results)

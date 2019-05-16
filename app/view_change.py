from assets.database import db_session
from assets.models import Data
import pandas as pd

#データベースから読み込み
data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates=[]
subscribers = []
reviews = []

for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)
diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(reviews).diff().values

print(diff_reviews)

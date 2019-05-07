from assets.database import db_session
from assets.database import init_db
from assets.models import Data
import datetime

init_db()

#create
date = datetime.date.today()
row1 = Data(date=date, subscribers=6500, reviews=210)
row2 = Data(date=date, subscribers=1500, reviews=220)
db_session.add(row1)
db_session.add(row2)
db_session.commit() #commitでデータベースに保存

#read
read1 = db_session.query(Data).all()[0].subscribers

#update
datum = db_session.query(Data).all()[0]
datum.subscribers = 1000
db_session.add(datum)
db_session.commit()

#dalete
datum = db_session.query(Data).filter_by(subscribers=1000).one()
db_session.delete(datum)
db_session.commit()
#全削除
#Data.query.delete()
print(db_session.query(Data).all())

import pandas as pd
from assets.database import db_session
import datetime

def read_data():
    from assets import models
    df = pd.read_csv('assets/data.csv')
    date = datetime.datetime.strptime(df.iloc[0,0], '%Y/%m/%d').date()
    for index, _df in df.iterrows():
        date = datetime.datetime.strptime(_df['date'], '%Y/%m/%d').date()
        row = models.Data(date=date, subscribers=_df['subscribers'], reviews=_df['reviews'])
        db_session.add(row)
        # print(date)
    db_session.commit()
# print(mydate)

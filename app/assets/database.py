# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os
import pandas as pd

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True , echo=True)
db_session = scoped_session(
                sessionmaker(
                    autocommit = False,
                    autoflush = False,
                    bind = engine
                )
             )
Base = declarative_base()
Base.query = db_session.query_property()

#データベース初期化
def init_db():
    import assets.models
    Base.metadata.create_all(bind=engine)

#初期データ読み込み
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

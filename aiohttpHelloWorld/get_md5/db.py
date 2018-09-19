from sqlalchemy import *

meta = MetaData()
client = Table(
    'client', meta,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('summ', String(200), nullable=False),
    Column('hash', String(200), nullable=False),
    Column('email_address', String(60)),
    Column('password', String(20), nullable=False),
    Column('reg_date', Date, nullable=False)
)

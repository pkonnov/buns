from sqlalchemy import create_engine, MetaData

from get_md5.db import client
from get_md5.settings import config


DSN = "postgresql://{postgres:{}@{localhost}:{5432}/{newbilling}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[client])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'user_id':'001',
         'user_name':'loh',
         'summ':'100',
         'hash':'38b3eff8baf56627478ec76a704e9b52',
         'email_address':'loh@ru.com',
         'password':'qwertyuiop',
         'reg_date':'2018-09-119 17:46:01.629+02'}
    ])
    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
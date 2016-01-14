# -*- coding: utf-8 -*-
from setting import DATABASE as DB
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://%s:%s@%s/%s' % (
    DB['user'],
    DB['password'],
    DB['host'],
    DB['database']), convert_unicode=True, encoding='utf-8')


mymetadata = MetaData(bind=engine)
Base = declarative_base(metadata=mymetadata)
# Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine))

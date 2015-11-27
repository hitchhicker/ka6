# -*- coding: utf-8 -*-
from setting import DATABASE as DB
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('postgresql://%s:%s@%s/%s' % (
	DB['user'],
	DB['password'],
	DB['host'],
	DB['database']), convert_unicode=True)

metadata = MetaData(bind=engine)

db_session = scoped_session(sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine))

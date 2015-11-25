from sqlalchemy import create_engine, MetaData, Table
from setting import DATABASE as DB
from sqlalchemy.orm import scoped_session, sessionmaker


database=DB['database']
user=DB['user']
password=DB['password']
host=DB['host']
engine = create_engine('postgresql://%s:%s@%s/%s' %
	(user, password, host, database), convert_unicode=True)
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

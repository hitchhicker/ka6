# -*- coding: utf-8 -*-
import psycopg2
from setting import DATABASE as DB


class Database(object):

    @classmethod
    def _connect(cls):
        """
        Create a connection to the PostgreSQL database
        """
        try:
            conn = psycopg2.connect(database=DB['database'], user=DB['user'],
                                    password=DB['password'], host=DB['host'],
                                    port=DB['port'])
        except:
            print ('Fail to connect to PostgreSQL')
        else:
            print ("Opened database successfully")
            return conn.cursor()

    @classmethod
    def fetchall(cls, sql):
        """
        Execute a fetch tyep statement
        :rtype list
        """
        with cls._connect() as cur:
            try:
                cur.execute(sql)
            except:
                print ('Fail to execute SQL %s' % sql)
            return cur.fetchall()

    @classmethod
    def execute_one(cls, sql):
        """
        Execute one SQL statement
        :param sql: string
        """
        with cls._connect() as cur:
            try:
                cur.execute(sql)
            except:
                print ('Fail to execute SQL %s' % sql)
                raise

    @classmethod
    def execute_all(cls, sqls):
        """
        Execute multiple statements
        :param sql: list of string
        """
        with cls._connect() as cur:
            try:
                for sql in sqls:
                    cur.execute(sql)
            except:
                print ('Fail to execute SQL %s' % sql)
                raise

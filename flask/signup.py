# -*- coding: utf-8 -*-
from models import User
from database import db_session
import hashlib


def add_user(email, password, name):
	pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
	new_user = User(email, pwd_hash, name)
	db_session.add(new_user)
	db_session.commit()

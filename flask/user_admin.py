# -*- coding: utf-8 -*-
from models import User
from database import db_session
import hashlib


def add_user(email, password, name):
	pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
	new_user = User(email, pwd_hash, name)
	print(new_user)
	db_session.add(new_user)
	db_session.commit()


def is_exist(email, password):
	"""Check user is exist or not
	:params email, password: string
	:rtype: result of login
	"""
	pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
	if User.query.filter_by(
		email=email, password=pwd_hash).all():
		return True
	else:
		False

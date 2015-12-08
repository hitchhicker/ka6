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


def get_user(email, password):
	"""Check user is exist or not
	:params email, password: string
	:rtype: list of User instance or None
	"""
	pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
	return User.query.filter_by(
		email=email, password=pwd_hash).one()

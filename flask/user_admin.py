# -*- coding: utf-8 -*-
from models import User, TagUser
from database import db_session
import hashlib


def add_user(email, password, name):
    pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    new_user = User(
        email=email,
        password=pwd_hash,
        name=name)
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


def add_user_tag(tag_name, user_email):
    """
    add ont tag for user
    """
    user = User.query.filter_by(email=user_email).one()
    tag = TagUser(tag_name=tag_name, user=user)
    db_session.add(tag)
    db_session.commit()

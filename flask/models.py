# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Sequence, Column, ForeignKey
from sqlalchemy.types import VARCHAR, CHAR, TIMESTAMP, BOOLEAN, TEXT
from sqlalchemy.orm import relationship

from database import db_session


Base = declarative_base()


class Location(Base):
	"""Sqlalchemy Location model"""
	__tablename__ = 'location'
	query = db_session.query_property()

	id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
	country = Column(VARCHAR(255), nullable=False)
	region = Column(VARCHAR(255), nullable=False)
	city = Column(VARCHAR(255), nullable=False)


class Address(Base):
	"""Sqlalchemy Address model"""
	__tablename__ = 'address'
	query = db_session.query_property()

	id = Column(Integer, Sequence('address_id_seq'), primary_key=True)
	area = Column(VARCHAR(255), nullable=False)
	street = Column(VARCHAR(255), nullable=False)
	id_location = Column(Integer, ForeignKey('location.id'))

	location = relationship('Location', foreign_keys=[id_location])


class User(Base):
    """Sqlalchemy User model"""
    __tablename__ = '_user'
    query = db_session.query_property()

    id = Column(Integer, Sequence('_user_id_seq'), primary_key=True)
    image = Column(VARCHAR(2083))
    email = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(CHAR(32), nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    id_location = Column(Integer, ForeignKey('location.id'))
    location = relationship('Location', foreign_keys=[id_location])
    tags = relationship('TagUser', primaryjoin='User.id==TagUser.id_user')


class Activity(Base):
	"""Sqlalchemy Activity model"""
	__tablename__ = 'activity'
	query = db_session.query_property()

	id = Column(Integer, Sequence('activity_id_seq'), primary_key=True)
	title = Column(VARCHAR(255), nullable=False)
	start_date = Column(TIMESTAMP, nullable=False)
	end_date = Column(TIMESTAMP, nullable=False)
	id_address = Column(Integer, ForeignKey('address.id'))
	allow_number = Column(Integer)
	like_number = Column(Integer, default=0)
	canceld = Column(BOOLEAN, default=False)

	address = relationship('Address', foreign_keys=[id_address])


class TagActivity(Base):
	"""Sqlalchemy TagActivity model"""
	__tablename__ = 'tagActivity'
	query = db_session.query_property()

	id = Column(Integer, Sequence('tagactivity_id_seq'), primary_key=True)
	tag_name = Column(VARCHAR(20), nullable=False)
	id_activity = Column(Integer, ForeignKey('activity.id'), nullable=False)

	activity = relationship('Activity', foreign_keys=[id_activity])


class TagUser(Base):
	"""Sqlalchemy TagActivity model"""
	__tablename__ = 'taguser'
	query = db_session.query_property()

	id = Column(Integer, Sequence('taguser_id_seq'), primary_key=True)
	tag_name = Column(VARCHAR(20), nullable=False)
	id_user = Column(Integer, ForeignKey('_user.id'), nullable=False)

	user = relationship('User', foreign_keys=[id_user])


class UserActivity(Base):
	"""Sqlalchemy UserActivity model"""
	__tablename__ = 'useractivity'
	query = db_session.query_property()

	id_user = Column(Integer, ForeignKey('_user.id'), nullable=False, primary_key=True)
	id_activity = Column(Integer, ForeignKey('activity.id'), nullable=False, primary_key=True)
	join_date = Column(TIMESTAMP, nullable=False)

	user = relationship('User', foreign_keys=[id_user])
	activity = relationship('Activity', foreign_keys=[id_activity])


class ActivityContent(Base):
	"""Sqlalchemy ActivityContent model"""
	__tablename__ = 'activitycontent'
	query = db_session.query_property()

	id_activity = Column(Integer, ForeignKey('activity.id'), primary_key=True)
	content = Column(TEXT, nullable=False)

	activity = relationship('Activity', foreign_keys=[id_activity])


class Comment(Base):
	"""Sqlalchemy Comment model"""
	__tablename__ = 'comment'
	query = db_session.query_property()

	id = Column(Integer, Sequence('comment_id_seq'), primary_key=True)
	id_activity = Column(Integer, ForeignKey('activity.id'), nullable=False)
	id_comment = Column(Integer, nullable=False)
	id_user = Column(Integer, ForeignKey('_user.id'), nullable=False)
	comment_date = Column(TIMESTAMP, nullable=False)
	body = Column(TEXT, nullable=False)

	activity = relationship('Activity', foreign_keys=[id_activity])
	user = relationship('User', foreign_keys=[id_user])

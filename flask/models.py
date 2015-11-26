from database import metadata, db_session
from sqlalchemy import Table
from sqlalchemy.orm import mapper


class User(object):
	query = db_session.query_property()

	def __init__(
		self,
		id,
		image,
		email,
		password,
		name):
		self.id = id
		self.image = image
		self.email = email
		self.password = password
		self.name = name

	def __repr__(self):
		return '<User %r>' % (self.name)

users = Table('_user', metadata, autoload=True)
mapper(User, users)


class Activity(object):
	query = db_session.query_property()

	def __init__(
		self,
		id,
		title,
		start_date,
		end_date,
		publish_date,
		allow_number,
		like_number,
		canceld):
		self.id = id
		self.title = title
		self.startDate = start_date
		self.endDate = end_date
		self.publishDate = publish_date
		self.allowNumber = allow_number
		self.likeNumber = like_number
		self.canceld = canceld

	def __repr__(self):
		return '<Activity %r>' % (self.title)

activity = Table('activity', metadata, autoload=True)
mapper(Activity, activity)


class Tag(object):
	query = db_session.query_property()

	def __init__(self, id, tag_name, id_activity):
		self.id = id
		self.tagName = tag_name
		self.idActivity = id_activity

	def __repr__(self):
		return '<Tag %r>' % (self.tagName)

tag = Table('tag', metadata, autoload=True)
mapper(Tag, tag)


class TagUser(object):
	query = db_session.query_property()

	def __init__(self, id, tag_name, id_user):
		self.id = id
		self.tagName = tag_name
		self.idUser = id_user

tag_user = Table('taguser', metadata, autoload=True)
mapper(TagUser, tag_user)


class UserActivity(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, join_date):
        self.idUser = id_user
        self.idActivity = id_activity
        self.joinDate = join_date

user_activity = Table('useractivity', metadata, autoload=True)
mapper(UserActivity, user_activity)


class ActivityContent(object):
    query = db_session.query_property()

    def __init__(self, id_activity, content):
        self.id_activity = id_activity
        self.content = content

activity_content = Table('activitycontent', metadata, autoload=True)
mapper(ActivityContent, activity_content)


class Comment(object):
    query = db_session.query_property()

    def __init__(
        self,
        id,
        id_activity,
        id_comment,
        id_user,
        comment_date,
        body):

        self.id = id
        self.idActivity = id_activity
        self.idComment = id_comment
        self.idUser = id_user
        self.commentDate = comment_date
        self.body = body

    def __repr__(self):
        return '<Comment %r >' % self.body

comment = Table('comment', metadata, autoload=True)
mapper(Comment, comment)

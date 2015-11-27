from database import metadata, db_session
from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship


class User(object):
	query = db_session.query_property()

	def __init__(
		self,
		image,
		email,
		password,
		name):
		self.image = image
		self.email = email
		self.password = password
		self.name = name

	def __repr__(self):
		return '<User %r>' % (self.name)


class TagUser(object):
    query = db_session.query_property()
    # user = relationship(
    #     'User',
    #     backref='User.id',
    #     primaryjoin='TagUser.id_user==User.id')

    def __init__(self, tag_name, id_user):
        self.tag_name = tag_name
        self.id_user = id_user

    def __repr__(self):
        return '<TagUser %r>' % (self.tag_name)

tag_user = Table('taguser', metadata, autoload=True)
users = Table('_user', metadata, autoload=True)

mapper(User, users, properties={
    'tags': relationship(TagUser)})
mapper(TagUser, tag_user, properties={
    'users': relationship(User)})


class Activity(object):
	query = db_session.query_property()

	def __init__(
		self,
		title,
		start_date,
		end_date,
		publish_date,
		allow_number,
		like_number,
		canceld):
		self.title = title
		self.start_date = start_date
		self.end_date = end_date
		self.publish_date = publish_date
		self.allow_number = allow_number
		self.like_number = like_number
		self.canceld = canceld

	def __repr__(self):
		return '<Activity %r>' % (self.title)

activity = Table('activity', metadata, autoload=True)
mapper(Activity, activity)


class TagActivity(object):
	query = db_session.query_property()

	def __init__(self, tag_name, id_activity):
		self.tag_name = tag_name
		self.id_activity = id_activity

	def __repr__(self):
		return '<Tag %r>' % (self.tagName)

tag_activity = Table('tagactivity', metadata, autoload=True)
mapper(TagActivity, tag_activity)


class UserActivity(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, join_date):
        self.id_user = id_user
        self.id_activity = id_activity
        self.join_date = join_date

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
        id_activity,
        id_comment,
        id_user,
        comment_date,
        body):

        self.id_activity = id_activity
        self.id_comment = id_comment
        self.id_user = id_user
        self.comment_date = comment_date
        self.body = body

    def __repr__(self):
        return '<Comment %r >' % self.body

comment = Table('comment', metadata, autoload=True)
mapper(Comment, comment)


class Following(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

following = Table('following', metadata, autoload=True)
mapper(Following, following)


class Follower(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

follower = Table('follower', metadata, autoload=True)
mapper(Follower, follower)


class ActivityFollowing(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

activity_following = Table('activity_following', metadata, autoload=True)
mapper(ActivityFollowing, activity_following)


class ActivityFollower(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

activity_follower = Table('activity_follower', metadata, autoload=True)
mapper(ActivityFollower, activity_follower)


class Friends(object):
    query = db_session.query_property()

    def __init__(self, id_user1, id_user2, add_date):
        self.id_user1 = id_user1
        self.id_user2 = id_user2
        self.add_date = add_date

friends = Table('friends', metadata, autoload=True)
mapper(Friends, friends)


class Invitation(object):
    query = db_session.query_property()

    def __init__(
        self,
        invitor,
        invited,
        id_activity,
        invite_date):
        self.invitor = invitor
        self.invited = invited
        self.id_activity = id_activity
        self.invite_date = invite_date

invitation = Table('invitation', metadata, autoload=True)
mapper(Invitation, invitation)


class Conversation(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, time):
        self.fromid = fromid
        self.toid = toid
        self.time = time

conversation = Table('conversation', metadata, autoload=True)
mapper(Conversation, conversation)


class Reply(object):
    query = db_session.query_property()

    def __init__(self, reply, time, conversation_id):
        self.reply = reply
        self.time = time
        self.conversation_id = conversation_id

reply = Table('reply', metadata, autoload=True)
mapper(Reply, reply)


class Broadcast(object):
    query = db_session.query_property()

    def __init__(
        self,
        fromid,
        toid,
        message,
        send_date):
        self.fromid = fromid
        self.toid = toid
        self.message = message
        self.send_date = send_date

broadcast = Table('broadcast', metadata, autoload=True)
mapper(Broadcast, broadcast)


class Click(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, click_date):
        self.id_user = id_user
        self.idActivity = id_activity
        self.click_date = click_date

click = Table('click', metadata, autoload=True)
mapper(Click, click)


class Search(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, search_date):
        self.id_uuser = id_user
        self.id_activity = id_activity
        self.search_date = search_date

search = Table('search', metadata, autoload=True)
mapper(Search, search)


class Like(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, like_date):
        self.id_uuser = id_user
        self.id_activity = id_activity
        self.likeate = like_date

like = Table('l1ke', metadata, autoload=True)
mapper(Like, like)

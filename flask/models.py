from database import metadata, db_session
from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship


class Location(object):
    query = db_session.query_property()

    def __init__(self, id_location, region, city):
        self.id_location = id_location
        self.region = region
        self.city = city

    def __repr__(self):
        return '<Location %r>' % (self.city)

location = Table('location', metadata, autoload=True)


class Address(object):
    query = db_session.query_property()

    def __init__(self, area, street, id_location):
        self.area = area
        self.street = street
        self.id_location = id_location

    def __repr__(self):
        return '<Address %r>' % (self.street)

address = Table('address', metadata, autoload=True)


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

users = Table('_user', metadata, autoload=True)


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


class TagActivity(object):
	query = db_session.query_property()

	def __init__(self, tag_name, id_activity):
		self.tag_name = tag_name
		self.id_activity = id_activity

	def __repr__(self):
		return '<Tag %r>' % (self.tagName)

tag_activity = Table('tagactivity', metadata, autoload=True)


class UserActivity(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, join_date):
        self.id_user = id_user
        self.id_activity = id_activity
        self.join_date = join_date

user_activity = Table('useractivity', metadata, autoload=True)


class UserLocation(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_location):
        self.id_user = id_user
        self.id_location = id_location

user_location = Table('userlocation', metadata, autoload=True)


class ActivityContent(object):
    query = db_session.query_property()

    def __init__(self, id_activity, content):
        self.id_activity = id_activity
        self.content = content

activity_content = Table('activitycontent', metadata, autoload=True)


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


class Following(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

following = Table('following', metadata, autoload=True)


class Follower(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

follower = Table('follower', metadata, autoload=True)


class ActivityFollowing(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

activity_following = Table('activity_following', metadata, autoload=True)


class ActivityFollower(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, follow_date):
        self.fromid = fromid
        self.toid = toid
        self.follow_date = follow_date

activity_follower = Table('activity_follower', metadata, autoload=True)


class Friends(object):
    query = db_session.query_property()

    def __init__(self, id_user1, id_user2, add_date):
        self.id_user1 = id_user1
        self.id_user2 = id_user2
        self.add_date = add_date

friends = Table('friends', metadata, autoload=True)


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


class Conversation(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, time):
        self.fromid = fromid
        self.toid = toid
        self.time = time

conversation = Table('conversation', metadata, autoload=True)


class Reply(object):
    query = db_session.query_property()

    def __init__(self, reply, time, conversation_id):
        self.reply = reply
        self.time = time
        self.conversation_id = conversation_id

reply = Table('reply', metadata, autoload=True)


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


class Click(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, click_date):
        self.id_user = id_user
        self.idActivity = id_activity
        self.click_date = click_date

click = Table('click', metadata, autoload=True)


class Search(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, search_date):
        self.id_uuser = id_user
        self.id_activity = id_activity
        self.search_date = search_date

search = Table('search', metadata, autoload=True)


class Like(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, like_date):
        self.id_uuser = id_user
        self.id_activity = id_activity
        self.likeate = like_date

like = Table('l1ke', metadata, autoload=True)

# configuration mapping
mapper(Location, location)
mapper(Address, address)
mapper(User, users, properties={
    'tags': relationship(TagUser),
    'activities': relationship(UserActivity),
    'comments': relationship(Comment),
    'clicks': relationship(Click),
    'searchs': relationship(Search),
    'likes': relationship(Like), })
mapper(Activity, activity, properties={
    'tags': relationship(TagActivity),
    'users': relationship(UserActivity),
    'contents': relationship(ActivityContent),
    'commnets': relationship(Comment),
    'clicks': relationship(Click),
    'searchs': relationship(Search),
    'likes': relationship(Like), })
mapper(TagUser, tag_user)
mapper(TagActivity, tag_activity)
mapper(UserActivity, user_activity)
mapper(UserLocation, user_location, properties={
    'users': relationship(User), })
mapper(ActivityContent, activity_content)
mapper(Comment, comment)
mapper(Following, following)
mapper(Follower, follower)
mapper(ActivityFollowing, activity_following)
mapper(ActivityFollower, activity_follower)
mapper(Friends, friends)
mapper(Invitation, invitation)
mapper(Conversation, conversation)
mapper(Reply, reply)
mapper(Broadcast, broadcast)
mapper(Click, click)
mapper(Search, search)
mapper(Like, like)

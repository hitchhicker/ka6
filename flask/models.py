# -*- coding: utf-8 -*-
from database import metadata, db_session
from sqlalchemy import Table
from sqlalchemy.orm import mapper, relationship


class Location(object):
    query = db_session.query_property()

    def __init__(self, country, region, city):
        self.id = None
        self.country = country
        self.region = region
        self.city = city

    def __repr__(self):
        return '<Location %r>' % (self.city)

location = Table('location', metadata, autoload=True)


class Address(object):
    query = db_session.query_property()

    def __init__(self, area, street, id_location):
        self.id = None
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
        email,
        password,
        name,
        id_location=None,
        image=None):
        self.id = None
        self.id_location = id_location
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
        canceld,
        id_address):
        self.id = None
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.publish_date = publish_date
        self.allow_number = allow_number
        self.like_number = like_number
        self.canceld = canceld
        self.id_address = id_address

    def __repr__(self):
        return '<Activity %r>' % (self.title)

activity = Table('activity', metadata, autoload=True)


class TagUser(object):
    query = db_session.query_property()

    def __init__(self, tag_name, id_user):
        self.id = None
        self.tag_name = tag_name
        self.id_user = id_user

    def __repr__(self):
        return '<TagUser %r>' % (self.tag_name)

tag_user = Table('taguser', metadata, autoload=True)


class TagActivity(object):
    query = db_session.query_property()

    def __init__(self, tag_name, id_activity):
        self.id = None
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
        self.id = None
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
        self.id = None
        self.invitor = invitor
        self.invited = invited
        self.id_activity = id_activity
        self.invite_date = invite_date

invitation = Table('invitation', metadata, autoload=True)


class Conversation(object):
    query = db_session.query_property()

    def __init__(self, fromid, toid, time):
        self.id = None
        self.fromid = fromid
        self.toid = toid
        self.time = time

conversation = Table('conversation', metadata, autoload=True)


class Reply(object):
    query = db_session.query_property()

    def __init__(self, reply, time, conversation_id):
        self.id = None
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
        self.id = None
        self.fromid = fromid
        self.toid = toid
        self.message = message
        self.send_date = send_date

broadcast = Table('broadcast', metadata, autoload=True)


class Click(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, click_date):
        self.id = None
        self.id_user = id_user
        self.idActivity = id_activity
        self.click_date = click_date

click = Table('click', metadata, autoload=True)


class Search(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, search_date):
        self.id = None
        self.id_user = id_user
        self.id_activity = id_activity
        self.search_date = search_date

search = Table('search', metadata, autoload=True)


class Like(object):
    query = db_session.query_property()

    def __init__(self, id_user, id_activity, like_date):
        self.id = None
        self.id_user = id_user
        self.id_activity = id_activity
        self.likeate = like_date

like = Table('l1ke', metadata, autoload=True)

# configuration mapping
mapper(Location, location)
mapper(Address, address)
mapper(User, users)
mapper(Activity, activity)
mapper(TagUser, tag_user)
mapper(TagActivity, tag_activity)
mapper(UserActivity, user_activity)
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

# configure foreign key relationship
User.tags = relationship(
    'Taguser',
    primaryjoin='User.id==Taguser.id_user')
User.activities = relationship(
    'UserActivity',
    primaryjoin='User.id==UserActivity.id_user')
Activity.tags = relationship(
    'TagActivity',
    primaryjoin='Activity.id==TagActivity.id_activity')

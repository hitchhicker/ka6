# from models import User, TagUser
from database import db_session
from models import User, TagUser
# tags = TagUser.query.filter_by(tag_name='amazing').all()
# for tag in tags:
# 	print(User.query.filter_by(id=tag.id_user).one())

# user = User.query.filter_by(email='yubokai@gmail.com').one()
# print(user)
# tag1 = TagUser('amazing', '1')
# tag2 = TagUser('amazing', '2')

# db_session.add(tag1)
# db_session.add(tag2)
# db_session.commit()

# tag = TagUser.query.filter_by(tag_name='amazing').all()

user = User.query.filter_by(name='yu').one()
for tag in user.tags:
	print(tag.tag_name)
# tag = TagUser(tag_name='amazing', user=user)
# db_session.add(tag)
# db_session.commit()

from models import User, TagUser
from database import db_session

tags = TagUser.query.filter_by(tag_name='amazing').all()
for tag in tags:
	print (User.query.filter_by(id=tag.id_user).one())

user = User.query.filter_by(name='yu').one()
print (user.tags)
# tag1 = TagUser('amazing', '1')
# tag2 = TagUser('amazing', '2')

# db_session.add(tag1)
# db_session.add(tag2)
# db_session.commit()

# tag = TagUser.query.filter_by(tag_name='amazing').all()

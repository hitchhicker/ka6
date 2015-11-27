from models import User, TagUser

tag = TagUser.query.filter_by(id_user=1).one()
print (tag.users)

user = User.query.filter_by(name='yu').one()
print (user.tags)

from models import User


me = User.query.filter_by(name='yu').first()
print (me.email)

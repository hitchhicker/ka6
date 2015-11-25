from database import Database

sql = 'SELECT * FROM User;'
print (Database.fetchall(sql))
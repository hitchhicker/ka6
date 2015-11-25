# -*- coding: utf-8 -*-
from flask import Flask
from database import db_session
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'postgresql://postgres:asd123zxc@localhost/ka6'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] =True  # what for ?

@app.route("/")
def home():
    return 'hello'  

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__== "__main__":
    app.run(debug=True)

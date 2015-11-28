# -*- coding: utf-8 -*-
from flask import Flask
from database import db_session

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route("/")
def home():
    return 'hello'


@app.route('/login')
def login():
	pass


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run()

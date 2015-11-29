# -*- coding: utf-8 -*-
from flask import Flask, request, session, flash, redirect,\
	render_template, url_for
from database import db_session

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET'])
def signup():
	try:
		step = request.args.get('step')
	except KeyError:
		# 404 eror TODO
		print ('error')
	if step == '1':
		return render_template('signup_step_1.html')
	elif step == 1:
		return render_template('signup_step_1.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	pass
    # error = None
    # if request.method == 'POST':
    #     if request.form['username'] != app.config['USERNAME']:
    #         error = 'Invalid username'
    #     elif request.form['password'] != app.config['PASSWORD']:
    #         error = 'Invalid password'
    #     else:
    #         session['logged_in'] = True
    #         flash('You were logged in')
    #         return redirect(url_for('show_entries'))
    # return render_template('login.html', error=error)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run()

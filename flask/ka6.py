# -*- coding: utf-8 -*-
from flask import Flask, request, session, flash, redirect,\
	render_template, url_for
from database import db_session
from user_admin import add_user, is_exist


app = Flask(__name__)
app.config.update(
    DEBUG=True,
)
app.secret_key = \
	b'\xac}|\xe3\x19=M\xc9\xc0\xf8\x04\x11k\x87\xa0-\xe0M\xe5Ua|\x92I'


@app.route("/")
def index():
	if 'user_name' in session:
		return render_template(
			'index.html',
			username=session['user_name'])
	return render_template('index.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
	try:
		step = request.values.get('step')
	except KeyError:
		# 404 eror TODO
		print('error')
	if step == '1':
		return render_template('signup_step_1.html')
	elif step == '2':
		try:
			email = request.values.get('email')
			password = request.values.get('password')
			name = request.values.get('nickname')
		except KeyError:
			print('key error')  # TODO
			raise
		print(email)
		print(password)
		print(name)
		add_user(email, password, name)
		return render_template('signup_step_2.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if is_exist(
			request.form['email'],
			request.form['password']):
			session['logged_in'] = True
			session['user_name'] = request.form['email']
			return redirect(url_for('index'))
		else:
			pass
	# return render_template('login.html', error=error)


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run()

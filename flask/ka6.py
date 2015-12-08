# -*- coding: utf-8 -*-
from flask import Flask, render_template
from database import db_session
import views


app = Flask(__name__)
app.config.update(
    DEBUG=True,
)
app.secret_key = \
	b'\xac}|\xe3\x19=M\xc9\xc0\xf8\x04\x11k\x87\xa0-\xe0M\xe5Ua|\x92I'

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/signup', view_func=views.signup, methods=['POST', ])
app.add_url_rule('/login', view_func=views.login, methods=['POST', ])
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/user/settings', view_func=views.settings)


# @app.errorhandler(404)
@app.route('/404')
def page_not_found():
    return render_template('404.html')


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run()

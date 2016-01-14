# -*- coding: utf-8 -*-
from flask import request, session, flash, redirect,\
    render_template, url_for
from user_admin import add_user, get_user, add_user_tag


def settings():
    add_user_tag('tag', 'yubokai@gmail.com')
    return render_template('settings.html')


def index():
    if 'user_name' in session:
        return render_template(
            'index.html',
            username=session['user_name'])
    return render_template('index.html')


def signup():
    try:
        step = request.values.get('step')
    except KeyError:
        print('error')
    if step == 'init':
        return render_template('signup.html')
    elif step == 'done':
        try:
            email = request.values.get('email')
            password = request.values.get('password')
            name = request.values.get('nickname')
        except KeyError:
            print('key error')  # TODO
            raise
        add_user(email, password, name)
        # TODO
        # send a mail to confirme
        user = get_user(email, password)
        session['logged_in'] = True
        session['user_name'] = user.name

        return redirect(url_for('index'))


def logout():
    session.pop('logged_in', None)
    session.pop('user_name', None)
    flash('You were logged out')
    return redirect(url_for('index'))


def login():
    user = get_user(
        request.form['email'],
        request.form['password'])
    if user:
        session['logged_in'] = True
        session['user_name'] = user.name
        return redirect(url_for('index'))
    else:
        pass
    # return render_template('login.html', error=error)

from flask import Flask, render_template, request, redirect, url_for, json, make_response, session, flash
import os
from datetime import datetime
from app.forms import LoginForm, ChangePasswordForm
from app import app
import random

def get_user_info():
    user_os = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return user_os, user_agent, current_time



@app.route('/')
def home():
    user_os, user_agent, current_time = get_user_info()
    return render_template('home.html', user_os=user_os, user_agent=user_agent, current_time=current_time)

@app.route('/about')
def about():
    return render_template('about.html',)

@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    filename = os.path.join(app.static_folder, 'data', 'auth.json')
    with open(filename) as auth_file:
        data = json.load(auth_file)

    json_name = data['name']
    json_password = data['password']

    if form.validate_on_submit():
        form_name = form.username.data
        form_password = form.password.data
        form_remember = form.remember.data

        if json_name == form_name and json_password == form_password:
            if form_remember:
                user_id = random.randint(1, 10000)
                session['userId'] = user_id
                session['name'] = form_name
                session['password'] = form_password
                flash("Вхід виконано", category=("success"))
                return redirect(url_for('info', user=session['name']))
            else:
                flash("Ви не позначили галочку запамʼятати, введіть дані ще раз", category=("warning"))
                return redirect(url_for('home'))
        else:
            flash("Вхід не виконано", category=("warning"))
            return redirect(url_for('login'))

    return render_template('login.html', form=form)
@app.route('/info', methods=['GET'])
def info():
    cookies = request.cookies
    form = ChangePasswordForm()

    return render_template('info.html', cookies=cookies, form=form)
@app.route('/logout')
def logout():
    session.pop('userId')
    session.pop('name')
    session.pop('password')
    return redirect(url_for("login"))

def set_cookie(key, value, max_age):
    response = make_response(redirect('info'))
    response.set_cookie(key, value, max_age=max_age)
    return response

def delete_cookie(key):
    response = make_response(redirect('info'))
    response.delete_cookie(key)
    return response


@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('key')
    value = request.form.get('value')
    max_age = int(request.form.get('max_age'))

    flash("Кукі додано", category=("success"))
    return set_cookie(key, value, max_age)
@app.route('/remove_cookie/', methods=['GET'])
@app.route('/remove_cookie/<key>', methods=['GET'])
def remove_cookie():

    key = request.args.get('key')

    if key:
        flash("Кукі видалено", category=("dark"))
        response = make_response(redirect(url_for('info')))
        response.delete_cookie(key)
        return response
    else:
        flash("Виникла помилка. Повідомте про ключ ", category=("info"))
        response = make_response(redirect(url_for('info')))
        return response

@app.route('/remove_all_cookies', methods=['GET'])
def remove_all_cookies():
    flash("Усі кукі видалено", category=("danger"))
    response = make_response(redirect(url_for('info')))
    cookies = request.cookies

    for key in cookies.keys():
        if key != 'session':
            response.delete_cookie(key)

    return response
@app.route('/change_password', methods=['POST'])
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        new_password = form.password.data
        confirm_new_password = form.confirm_password.data
        if new_password != '':
            if new_password == confirm_new_password:
                session['password'] = new_password

                filename = os.path.join(app.static_folder, 'data', 'auth.json')
                with open(filename) as auth_file:
                    data = json.load(auth_file)

                new_admin_data = {
                    'name': data['name'],
                    'password': new_password
                }

                new_passwd_json = json.dumps(new_admin_data, indent=2)

                with open(filename, "w") as outfile:
                    outfile.write(new_passwd_json)

                flash("Пароль успішно змінено", category=("success"))
                return redirect(url_for('info'))

            flash("Ви не змінили пароль", category=("danger"))
            return redirect(url_for('info'))

    flash("Ви не ввели пароль. Спробуйте ще раз", category=("danger"))
    return redirect(url_for('info'))
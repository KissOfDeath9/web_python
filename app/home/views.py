from flask import render_template

from . import home_blueprint

@home_blueprint.route('/home')
@home_blueprint.route('/')
def home():
    return render_template('home.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')

@home_blueprint.route('/skills')
def skills():
    return render_template('skills.html')
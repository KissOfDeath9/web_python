from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)


from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    user_os = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os_info = f"Операційна система: {os.name}"
    return render_template('home.html', title='Головна', user_os=user_os, user_agent=user_agent, current_time=current_time, os_info=os_info)

@app.route('/about')
def about():
    user_os = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os_info = f"Операційна система: {os.name}"
    return render_template('about.html', title='Про мене', user_os=user_os, user_agent=user_agent, current_time=current_time, os_info=os_info)

@app.route('/skills')
def skills():
    user_os = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os_info = f"Операційна система: {os.name}"
    return render_template('skills.html', title='Навички', user_os=user_os, user_agent=user_agent, current_time=current_time, os_info=os_info)

if __name__ == '__main__':
    app.run(debug=True)

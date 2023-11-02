from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Th1sIsAS3cr3tK3y'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedbacks.db'
db = SQLAlchemy(app)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    comment = db.Column(db.Text)

with app.app_context():
    db.create_all()

from flask import render_template, flash, redirect, url_for
from forms import FeedbackForm

@app.route('/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()

    if form.validate_on_submit():
        name = form.name.data
        comment = form.comment.data

        feedback_entry = Feedback(name=name, comment=comment)
        db.session.add(feedback_entry)
        db.session.commit()

        flash('Ваш відгук був успішно збережений!', 'success')
        return redirect(url_for('feedback'))

    feedbacks = Feedback.query.all()
    return render_template('feedback.html', form=form, feedbacks=feedbacks)

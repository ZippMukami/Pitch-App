from datetime import datetime
from calendar import c
from email.policy import default
from turtle import title
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from forms import RegistrationForm, LoginForm

app = Flask (__name__)
app.config['SECRET_KEY'] = '594910733c8c780091c2cf7dd0eb0bed'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    pitches = db.relationship('Pitch', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Pitch('{self.title}', '{self.date_posted}')"


 

pitches = [
    {
        'author': "Jane Andy",
        'title': "Pitch Post 1",
        'content': "First pitch Content",
        'date_posted':"April 13th, 2022"
    }, 
    {
        'author': "Laurel Md",
        'title': "Pitch Post 2",
        'content': "Second pitch Content",
        'date_posted':"January 2nd, 2022"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')   

@app.route("/register", methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)


@app.route("/login", methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pitch.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)    

if __name__=='__main__':
    app.run(debug=True)
     

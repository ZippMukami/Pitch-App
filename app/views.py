from email.mime import image
from encodings import utf_8
from fileinput import filename
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Pitch
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)


@app.route("/login", methods= ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check email and password', 'danger')
    return render_template('login.html', title = 'Login', form=form)    

@app.route("/logout")
def logout():  
    logout_user()  
    return redirect(url_for('home'))

    
@app.route("/account")
@login_required
def account():  
    image_file = url_for('static', filename='default_dp/' + current_user.image_file)
    return render_template('account.html', title ='Account', image_file = image_file)    

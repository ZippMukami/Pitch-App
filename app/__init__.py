from turtle import title
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask (__name__)

app.config['SECRET_KEY'] = '594910733c8c780091c2cf7dd0eb0bed'

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
     
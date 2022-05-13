from turtle import title
from flask import Flask, render_template, url_for
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
def name():
    return render_template('home.html', pitches=pitches)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')   

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)    

if __name__=='__main__':
    app.run(debug=True)
     
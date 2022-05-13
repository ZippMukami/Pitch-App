from turtle import title
from flask import Flask, render_template, url_for
app = Flask (__name__)

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

if __name__=='__main__':
    app.run(debug=True)
     
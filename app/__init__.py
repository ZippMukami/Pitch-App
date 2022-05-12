from flask import Flask, render_template
app = Flask (__name__)

pitches = [
    {
        'author': "Jane Andy",
        'title': "Pitch Post 1",
        'content': "First pitch Content",
        'date_posted':"April 13th, 2022"
    }
]


@app.route("/")
@app.route("/home")
def name():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')   

if __name__=='__main__':
    app.run(debug=True)
     
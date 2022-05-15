from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config['SECRET_KEY'] = '594910733c8c780091c2cf7dd0eb0bed'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'

db = SQLAlchemy(app)

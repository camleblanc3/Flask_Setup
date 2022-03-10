#flask routes control what content is on what url
#generl structure of flask route is a function with a decorator

#first route: display index.html when user navigates to base url
from app import app

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/page')
def page():
    return render_template('page.html')
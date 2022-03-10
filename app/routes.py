#flask routes control what content is on what url
#generl structure of flask route is a function with a decorator

#first route: display index.html when user navigates to base url
from app import app

from flask import render_template

@app.route('/')
def home():
    westas = ['lebron james', 'stephen curry', 'andrew wiggins', 'ja morant', 'nikola jokic', 'devin booker', 'rudy gobert', 'chris paul', 'draymond green', 'donovan mitchell', 'luka doncic', ' dejounte murray', 'karl-anthony towns']
    eastas = ['kevin durant', 'trae young', 'jayson tatum', 'joel embiid', 'demar derozan', 'giannis antetokounmpo', 'lamelo ball', 'darius garland', 'james harden', 'zach lavine', 'fred vanvleet', 'jimmy butler', 'khris middleton', 'jarrett allen']
    return render_template('index.html', westas = westas, eastas = eastas)


@app.route('/page')
def page():
    return render_template('page.html')
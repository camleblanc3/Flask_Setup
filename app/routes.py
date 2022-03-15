#flask routes control what content is on what url
#generl structure of flask route is a function with a decorator

#first route: display index.html when user navigates to base url


from app import app

from flask import render_template,request
from .forms import PokeForm

from .services import pokeJersey
import requests as r

@app.route('/')
def home():
    westas = ['lebron james', 'stephen curry', 'andrew wiggins', 'ja morant', 'nikola jokic', 'devin booker', 'rudy gobert', 'chris paul', 'draymond green', 'donovan mitchell', 'luka doncic', ' dejounte murray', 'karl-anthony towns']
    eastas = ['kevin durant', 'trae young', 'jayson tatum', 'joel embiid', 'demar derozan', 'giannis antetokounmpo', 'lamelo ball', 'darius garland', 'james harden', 'zach lavine', 'fred vanvleet', 'jimmy butler', 'khris middleton', 'jarrett allen']
    return render_template('index.html', westas = westas, eastas = eastas)


@app.route('/page', methods=['GET', 'POST'])
def page():
    form = PokeForm()
    if request.method == 'POST':
        try:
            data = r.get(f'https://pokeapi.co/api/v2/pokemon/{form.pokename.data}').json()
            poke = data
        except:
            poke = form.pokename.data
        return render_template('page.html', form = form, poke = poke)
    return render_template('page.html', form = form, poke = None)
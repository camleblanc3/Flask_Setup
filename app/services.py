import requests as r


def pokeJersey():
    d={}
    for x in range(3,100,3):
        result = r.get(f'https://pokeapi.co/api/v2/pokemon/{x}')
        data = result.json()
        if data['game_indices'][0]['version']['name'] == 'red':
            d['name'] = data['name']
            d['id'] = data['id']
            d['height'] = data['height']
            d['ability'] = data['abilities'][0]['ability']['name']
            d['type'] = data['types'][0]['type']['name']
            return d
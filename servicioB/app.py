import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pokemon/<name>')
def get_pokemon_info(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [t['type']['name'] for t in data['types']],
            'abilities': [a['ability']['name'] for a in data['abilities']]
        }
        return f'El pokemon {pokemon_info["name"]}, es de tipo  {pokemon_info["types"]}, pesa {pokemon_info["weight"]} con una altura de {pokemon_info["height"]}\nSus habilidades son  {pokemon_info["abilities"]}'
    else:
        return f'No se pudo encontrar información para el Pokémon {name}', 404

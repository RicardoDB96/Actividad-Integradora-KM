import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def weather():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=25.67507&lon=-100.31847&appid=c6507f447d298eb6dda98a8e0b415a9a')
    data = response.json()
    weather_description = data['weather'][0]['description']
    return f'El clima actual es: {weather_description}'

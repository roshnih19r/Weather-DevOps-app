from flask import Blueprint, render_template, request, jsonify
import requests
import os

main = Blueprint('main', __name__)

API_KEY = "8e97d8224467e433006f7b55ce77c23d"

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather_info = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed']
        }
        return render_template('index.html', weather=weather_info)
    else:
        return render_template('index.html', error="City nahi mili!")

@main.route('/health')
def health():
    return jsonify({"status": "healthy"})
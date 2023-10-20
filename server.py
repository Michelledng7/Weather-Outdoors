from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from datetime import datetime


app = Flask(__name__)

@app.route('/') #homepage
@app.route('/index')
def index():  #return for the route
    return render_template('index.html')
    


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # check for empty strings or string with spaces
    if not bool(city.strip()):
        city = "Sydney"
    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template('weather.html', 
                           current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                           location = weather_data["name"],
                           country = weather_data['sys']['country'],
                           status=weather_data["weather"][0]["description"].capitalize(),
                           wind = f"{weather_data['wind']['speed']}",
                           temp=f"{weather_data['main']['temp']:.1f}",
                           feels_like=f"{weather_data['main']['feels_like']:.1f}")

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)   



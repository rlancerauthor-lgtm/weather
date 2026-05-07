from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    weather_data = get_current_weather(city)
    if weather_data:
        return render_template('index.html', title=weather_data["name"], status=weather_data['weather'][0]['description'].capitalize(), temp=f"{weather_data['main']['temp']:.1f}", feels_like=f"{weather_data['main']['feels_like']:.1f}")
    else:
        return render_template('index.html', title=city, status='Error fetching weather data', temp='N/A', feels_like='N/A')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
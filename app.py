from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods = ['POST', 'GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q' : requests.form.get("city"),
        'appid' : requests.form.get("appid"),
        'units' : requests.form.get("units")
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"


if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 5002)
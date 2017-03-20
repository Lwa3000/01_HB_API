from flask import Flask, request, render_template
from random import choice, randint
import urllib2
import json

from pprint import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/result')
# def result():
#     if forecastday=='rain':
#         return render_template("rainny.html")
#     else:
#         return render_template("notrainny.html")


@app.route('/getlocation')
def get_location():
    #Get location, pass it to the API
    location = request.args.get("location")
    location=location.replace(' ','_')
    state = request.args.get("state")
    if location == 'rain':
        forecasticon_url='/static/rain.jpg'
        return render_template("rainny.html", location='', icon=forecasticon_url, temp='', day='')
    elif state == "":
        url_part1='http://api.wunderground.com/api/65978e6c05a5014a/forecast/geolookup/conditions/q/'
        url_lastpart='.json'
        #Using lena's api key: 65978e6c05a5014a
        f = urllib2.urlopen(url_part1+location+url_lastpart)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        city = parsed_json['location']['city']
        state = parsed_json['location']['state']
        temp_f = parsed_json['current_observation']['temp_f']
        forecastday = parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon']
        forecasticon_url=parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon_url']
        day=parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
        f.close()

        if forecastday=='rain' or location =='rain':
            return render_template("rainny.html", location=location, icon=forecasticon_url, temp=temp_f, day=day)
        else:
            return render_template("notrainny.html", location=location, icon=forecasticon_url, temp=temp_f, day=day)
    else:
        location =state+'/'+location
        url_part1='http://api.wunderground.com/api/65978e6c05a5014a/forecast/geolookup/conditions/q/'
        url_lastpart='.json'
        #Using lena's api key: 65978e6c05a5014a
        f = urllib2.urlopen(url_part1+location+url_lastpart)
        json_string = f.read()
        parsed_json = json.loads(json_string)
        city = parsed_json['location']['city']
        state = parsed_json['location']['state']
        temp_f = parsed_json['current_observation']['temp_f']
        forecastday = parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon']
        forecasticon_url=parsed_json['forecast']['txt_forecast']['forecastday'][0]['icon_url']
        day=parsed_json['forecast']['txt_forecast']['forecastday'][0]['title']
        f.close()

        if forecastday=='rain' or location =='rain':
            return render_template("rainny.html", location=location, icon=forecasticon_url, temp=temp_f, day=day)
        else:
            return render_template("notrainny.html", location=location, icon=forecasticon_url, temp=temp_f, day=day)


if __name__ == "__main__":
    app.run(debug=True)

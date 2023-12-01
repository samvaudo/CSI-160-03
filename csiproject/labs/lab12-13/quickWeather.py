#! python3
# quickWeather.py - Prints the weather for a location on input

import json
import requests
import sys

api_key = 'c1e469faee850df34a1c55825f48e8a1'


# Gets location from input
def getLocation():
    state = str(input('Enter the state name, in two-letter format (ex. CA for California):'))
    city = str(input('Enter the city name, including spaces (ex. San Fransisco):'))
    loc = city + ',' + state
    return loc


def downloadWeatherAPI(loc):
    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'https://api.openweathermap.org/data/2.5/forecast?q=%sappid=%s' % (loc, api_key)
    response = requests.get(url)
    weather = json.loads(response.text)
    if weather["cod"] != 200:
        print(weather)
        print("Something went wrong, please try again.")
        sys.exit()
    else:
        return weather


def print3DayForecast(weather, loc):
    w = weather['list']
    print('Current weather in %s:' % loc)
    print(str(w[0]['main']['temp']) + 'F today currently, high of', str(w[0]['main']['temp_max']) + 'F and low of',
          str(w[0]['main']['temp_min']) + 'and a humidity of', str(w[0]['main']['humidity']) + '%')
    print('Currently there is', w[0]['weather']['main'], 'at', loc)
    print()
    print('Tomorrow:')
    print(str(w[1]['main']['temp']) + 'F tomorrow, high of', str(w[1]['main']['temp_max']) + 'F and low of',
          str(w[1]['main']['temp_min']) + 'and a humidity of', str(w[1]['main']['humidity']) + '%')
    print('Tomorrow there will be', w[1]['weather']['main'], 'at', loc)
    print()
    print('Day after tomorrow:')
    print(str(w[2]['main']['temp']) + 'F two days from now, high of', str(w[2]['main']['temp_max']) + 'F and low of',
          str(w[2]['main']['temp_min']) + 'and a humidity of', str(w[2]['main']['humidity']) + '%')
    print('Two days from now there will be', w[1]['weather']['main'], 'at', loc)


location = getLocation()
weatherData = downloadWeatherAPI(location)
print3DayForecast(weatherData,location)


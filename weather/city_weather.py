import json
import os
from datetime import datetime

user_api = os.environ['current_weather_data']

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appids=" + user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

print(api_data)


def weather():
    if api_data['cod'] == '404':
        print("invalid City: {}, Please check your city name".format(loaction))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d, %b, %Y | %I:%M:%S %p")

    print("weather stats for - {}  ||  {}".format(loaction.upper(), date_time))

    print("current temp is {:.2f} deg C".format(temp_city))

    print("current weather desc :", weather_desc)
    print("current Humidity     :", hmdt, '%')
    print('current wind speed   :', wind_spd, 'kmph')


if __name__ == '__main__':

    location = input("Enter city name:  ")
    weather()

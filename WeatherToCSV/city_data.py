import csv
import json
from urllib.request import urlopen

header = ['Name', 'Longitude', 'Latitude', 'Temperature']


def get_city(CityName):
    url1 = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    url = url1 + CityName
    response = urlopen(url)

    data_json = {"record": json.loads(response.read())}

    return data_json


def write_csv(data_json):
    with open('data1.csv', 'w') as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)
        for item in data_json.values():
            csv_file.writerow([item['name'], item['coord']['lon'], item['coord']['lat'],
                               item['main']['temp']])

        return {'data1.csv file updated successfully'}


if __name__ == '__main__':
    city = input("Enter your city name :\n")
    x = get_city(city)
    print(x)
    update = write_csv(x)
    print(update)

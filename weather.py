 ## Weather app that pulls data from OpenWeatherAPI & prints it out to CSV

# 1. Get API
# 2. Test API using URL - http://api.openweathermap.org/data/2.5/weather?q=Offaly,Ireland&APPID=API_HERE
# 3. Define API Key Variable
# 4. Make GET Request using requests module
# 5. Convert JSON to formatted String using regex

import os # For checking file size
import time # For time stamps
import requests # For get requests

API = "API_HERE"

link = "http://api.openweathermap.org/data/2.5/weather?units=metric&q=offaly,Ireland&APPID=API_HERE"

data = requests.get(link).json()
temp = data["main"]["temp"]
location_name = data["name"]

# --- Sample Dictionary Output --- #

# {'coord': {'lon': -7.6253, 'lat': 52.0881}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 286.82, 'feels_like': 286.64, 'temp_min': 286.53, 'temp_max': 288.46, 'pressure': 1025, 'humidity': 92}, 'visibility': 10000, 'wind': {'speed': 0.45, 'deg': 201, 'gust': 0.45}, 'clouds': {'all': 99}, 'dt': 1685225474, 'sys': {'type': 2, 'id': 2039644, 'country': 'IE', 'sunrise': 1685161273, 'sunset': 1685219661}, 'timezone': 3600, 'id': 2964528, 'name': 'Dungarvan', 'cod': 200}

temperature_csv_file_path = "/Users/username/Desktop/Weather-API-Project-RASPBERRYPI/temperature_data.csv"

try:
    with open(temperature_csv_file_path, "a+") as temperature_csv_file:
        if (os.stat(temperature_csv_file_path).st_size == 0):
            temperature_csv_file.write("Time,Temperature (°C),Location\r\n")

        # Sub in temp + time into parentheses
        temperature_csv_file.write("{},{},{}\r\n".format(time.strftime("%H:%M"),temp,location_name))
        print("Successfully written temperature to file: " + "temperature_data.csv")

except Exception as e:
    print("Error writing to file " + str(e))
            
        



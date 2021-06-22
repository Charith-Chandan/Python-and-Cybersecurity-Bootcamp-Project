# Name = Rudra Charith Chandan
# mail id = charithchandanr@gmail.com

import requests
from datetime import datetime


api_key = 'f75057935b3884f7385a8b1d343ed6ef'
# My API Key from openwethermap.org
location = input("Enter the city name: ")
# tacking the location form the user.

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data.
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

info = open('Temperaturedata.txt','w')
# Creates a text file if doesn't exsist or writes into the text file if it exsist.

info.write("-------------------------------------------------------------\n")
info.write ("Weather Status at {}  on {}\n".format(location.upper(), date_time))
# for writing weather status of a particular place at particular time and date in to text file.
info.write ("-------------------------------------------------------------\n")

info.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
# for writing current temperature in to text file.
info.write("Current weather desc  : {}\n".format(weather_desc))
# for writing current Weather in to text file.
info.write("Current Humidity      : {} %\n".format(hmdt))
# for writing current percentage of Humidity in to text file.
info.write("Current wind speed    : {} KMPH".format(wind_spd))
# for writing current wind speed in to text file.
info.close()
# for closing the text file which has been opened.


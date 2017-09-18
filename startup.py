#!/usr/bin/env python3
#stupid script I made to practice connecting to APIs
import requests
import json
from datetime import datetime 

current = datetime.now()
month = ["January", "Februray", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_num = current.month
day = str(current.day)
year = str(current.year)

hour = str(current.hour % 12)
minute = str(current.minute)
second = str(current.second)

#currently the URL is hardcoded. I could make it search by city and have the user enter the city on login
api_url = 'http://api.openweathermap.org/data/2.5/weather?id=4990729&mode=json&units=imperial&APPID=' + str('534fbf2240e048e05af1f52cab007535')

r = requests.get(api_url)
r.raise_for_status()

weather = json.loads(r.content)

wet1 = weather['weather'][0]['description']
wet2 = weather['main']['temp']
wet3 = weather['main']['temp_min']
wet4 = weather['main']['temp_max']
wet5 = weather['name']

loc = "Current weather for " + wet5 + ":"
desc = "Description: " + str(wet1)
cur_temp = "Current temp in: " + str(wet2)
min_temp = "Min temp: " + str(wet3)
max_temp = "Max temp: " + str(wet4)

out1 = "Today's date is " + month[month_num - 1] + " " + day + ", " + year
out2 = "The current time is " + hour +":" + minute + ":" + second
print(out1)
print(out2)
print(loc)
print(desc)
print(cur_temp)
print(max_temp)
print(min_temp)
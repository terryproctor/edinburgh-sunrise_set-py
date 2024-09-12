import requests
import datetime as dt

#Edinburgh latitude and longitude
MY_LAT = 55.953251
MY_LONG = -3.188267

my_params = {
            "lat" : MY_LAT,
            "lng" : MY_LONG,
            "formatted" : 0,
            }

response = requests.get('https://api.sunrise-sunset.org/json', params=my_params)
response.raise_for_status()

now = dt.datetime.now()
results = response.json()["results"]
sunrise = results["sunrise"][11:16].split(":")
sunset = results["sunset"][11:16].split(":")

now_time = {
            "hour" : now.hour, 
            "minute" : now.minute
            }

def is_daylight():
    if now_time["hour"] < int(sunrise[0]) or now_time["hour"] > int(sunset[0]):
        return False
    elif now_time["hour"] == int(sunrise[0]):
        if now_time["minute"] <  int(sunrise[1]):
            return False
    elif now_time["hour"] == int(sunset[0]):
        if now_time["minute"] >=  int(sunrise[1]):
            return False    
    else:
        return True                             

print(is_daylight()) 
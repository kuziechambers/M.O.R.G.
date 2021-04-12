from datetime import datetime as datetime
import datetime as dt
import pytz
import requests, json
from constants_sound import get_degrees_sound, sounds, time_sounds, degrees_sounds, play_sound
from constants_time import time_to_sound

# base URL
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lat = "32.844021"
lon = "-97.143066"
city_id = "4673094"
api_key = "fb3cc780290172e22840d597abea0445"

# updating the URL
URL = base_url + "lat=" + lat + "&lon=" + lon + "&units=imperial" + "&exclude=minutely" + "&appid=" + api_key

# # HTTP request
# response = requests.get(URL)


def get_current_temp():
    temp_response = requests.get(URL)
    temp_data = temp_response.json()
    temp_current = temp_data['current']
    temp_value = str(temp_current['temp'])
    temp_value = temp_value[0:2]
    return int(temp_value)

def get_low_temp():
    low_response = requests.get(URL)
    low_data = low_response.json()
    days = low_data['daily']
    today_min = str(days[0]['temp']['min'])
    temp_value = today_min[0:2]
    return int(temp_value)

def get_high_temp():
    high_response = requests.get(URL)
    high_data = high_response.json()
    days = high_data['daily']
    today_max = str(days[0]['temp']['max'])
    temp_value = today_max[0:2]
    return int(temp_value)

def get_weekend_temp():
    high_response = requests.get(URL)
    high_data = high_response.json()
    days = high_data['daily']
    saturday_min = str(days[1]['temp']['min'])
    saturday_max = str(days[1]['temp']['max'])
    sunday_min = str(days[2]['temp']['min'])
    sunday_max = str(days[2]['temp']['max'])
    saturday_min = saturday_min[0:2]
    saturday_max = saturday_max[0:2]
    sunday_min = sunday_min[0:2]
    sunday_max = sunday_max[0:2]
    return [int(saturday_min), int(saturday_max), int(sunday_min), int(sunday_max)]


def get_rain():
    try:
        rain_response = requests.get(URL)
        rain_data = rain_response.json()
        rain_hours = rain_data['hourly']

        tomorrow_date = datetime.today().date() + dt.timedelta(days=1)
        tomorrow_fiveam = datetime.strptime(str(tomorrow_date) + " 05:00:00", '%Y-%m-%d %H:%M:%S')

        for hour in rain_hours:
            d = datetime.fromtimestamp(hour['dt'])
            for item in hour['weather']:
                main_weather = item['main']
                if str(main_weather) == "Rain" and d < tomorrow_fiveam:
                    return str(d.time())
    except:
        return str("none")


def weekend_weather_update(temp_list):
    current_temp_degrees = get_current_temp()
    low_temp_degrees = get_low_temp()
    high_temp_degrees = get_high_temp()
    saturday_low_sound = get_degrees_sound(temp_list[0])
    saturday_high_sound = get_degrees_sound(temp_list[1])
    sunday_low_sound = get_degrees_sound(temp_list[2])
    sunday_high_sound = get_degrees_sound(temp_list[3])
    rain_time = get_rain()

    play_sound(sounds['s_enjoyweekendweather'])

    play_sound(sounds['s_saturdaylow'])
    play_sound(saturday_low_sound)
    play_sound(degrees_sounds['s_degrees'])
    play_sound(sounds['s_temphigh'])
    play_sound(saturday_high_sound)

    play_sound(sounds['s_sundaylow'])
    play_sound(sunday_low_sound)
    play_sound(degrees_sounds['s_degrees'])
    play_sound(sounds['s_temphigh'])
    play_sound(sunday_high_sound)


def weather_update():
    current_temp_degrees = get_current_temp()
    low_temp_degrees = get_low_temp()
    high_temp_degrees = get_high_temp()
    current_temp_sound = get_degrees_sound(current_temp_degrees)
    low_temp_sound = get_degrees_sound(low_temp_degrees)
    high_temp_sound = get_degrees_sound(high_temp_degrees)
    rain_time = get_rain()

    play_sound(sounds['s_temprightnow'])
    play_sound(current_temp_sound)
    play_sound(degrees_sounds['s_degrees'])
    play_sound(sounds['s_templow'])
    play_sound(low_temp_sound)
    play_sound(sounds['s_temphigh'])
    play_sound(high_temp_sound)
    if rain_time != "none":
        rain_sound = time_to_sound(rain_time)
        play_sound(sounds['s_rainchance'])
        play_sound(rain_sound)



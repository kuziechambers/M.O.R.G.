from datetime import datetime as datetime
import datetime as dt
#import pytz
import requests, json
#from playsound import playsound
from constants import sounds, play_sound
from events_ibm import play_response
#from events_sound import fx_to_file, play_fx_file

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
#try:
    rain = False
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
                time_string = str(d.strftime("%I:%M %p"))
                rain = True
                if time_string[:1] == "0":
                    date_P = time_string[1:2] + time_string[-2:]
                if time_string[:1] != "0":
                    date_P = time_string[0:2] + time_string[-2:]
                if date_P == "12AM":
                    date_P = "Midnight"

    if rain is True:
        return date_P
    else:
        return str("none")
#except:
#    return str("none")


def weekend_weather_update(temp_list):
    saturday_low = temp_list[0]
    saturday_high = temp_list[1]
    sunday_low = temp_list[2]
    sunday_high = temp_list[3]
    weather_text = "The low temperature for Saturday is <break strength='weak'></break>"\
                   + str(saturday_low)\
                   + " degrees, <break strength='weak'></break> and the high is <break strength='weak'></break>"\
                   + str(saturday_high)\
                   + ". <break strength='weak'></break> On Sunday the low temperature is projected to be <break strength='weak'></break>"\
                   + str(sunday_low) \
                   + " degrees, <break strength='weak'></break> and the projected high is <break strength='weak'></break>" \
                   + str(sunday_high) \
                   + "."

    play_sound(sounds['s_enjoyweekendweather'])
    play_response(weather_text)


def weather_update():
    current_temp_degrees = get_current_temp()
    print(str(current_temp_degrees))
    low_temp_degrees = get_low_temp()
    print(str(low_temp_degrees))
    high_temp_degrees = get_high_temp()
    print(str(high_temp_degrees))
    rain_time = get_rain()
    print(str(rain_time))
    if rain_time != "none":
        weather_text = "The temperature right now is <break strength='weak'></break>"\
                       + str(current_temp_degrees)\
                       + " degrees. The high for today is <break strength='weak'></break>"\
                       + str(high_temp_degrees)\
                       + ", and the low is <break strength='weak'></break>"\
                       + str(low_temp_degrees)\
                       + ". There is a chance of rain beginning around <break strength='weak'></break>" \
                       + str(rain_time) + "."
    else:
        weather_text = "The temperature right now is "\
                       + str(current_temp_degrees)\
                       + " degrees. The high for today is "\
                       + str(high_temp_degrees)\
                       + ", and the low is "\
                       + str(low_temp_degrees)\
                       + ". At the moment, there is no expected rain today."

    print(weather_text)
    play_response(weather_text)






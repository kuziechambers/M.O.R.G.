import json
import os
import random

import requests
import simpleaudio as audio

from constants import LIGHT_PAYLOADS, SOUNDS, TIME_SOUNDS


# play sound function
def play_sound(sound_file):
    # playsound(sound_file)
    audio.WaveObject.from_wave_file(sound_file).play().wait_done()


def play_weather_report_sound():
    weather_report_phrases = ["s_weatherreport1",
                              "s_weatherreport2",
                              "s_weatherreport3"]

    rint = random.randint(0, 2)
    path = weather_report_phrases[rint]
    play_sound(SOUNDS[path])


# turn on lights functions
def bright_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(LIGHT_PAYLOADS['bright_payload']))


def concentrate_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))


def morning_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps({"on": True, "bri": 254, "hue": 8645, "sat": 114}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps({"on": True, "bri": 127, "hue": 8645, "sat": 114}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps({"on": True, "bri": 178, "hue": 8645, "sat": 114}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps({"on": True, "bri": 178, "hue": 8645, "sat": 114}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps({"on": True, "bri": 127, "hue": 8645, "sat": 114}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps({"on": True, "bri": 254, "hue": 8645, "sat": 114}))


def dim_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(LIGHT_PAYLOADS['dim_payload']))


def all_lights_off():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(LIGHT_PAYLOADS['off_payload']))


def turn_on_light(text):
    light_id = 0
    light_id_2 = 0
    if "bedroom lamp" in text or "bedroom light" in text:
        light_id = 1
    if "mirror light" in text or "mirror lamp" in text:
        light_id = 5
    if "ceiling light" in text:
        light_id = 7
        light_id_2 = 8
    if "studio light" in text or "studio lamp" in text or "office light" in text or "office lamp" in text:
        light_id = 9
    if "tv lights" in text:
        light_id = 10
        light_id_2 = 11
    if "table lamp" in text or "table light" in text or "living room lamp" in text or "living room light" in text:
        light_id = 12
    if "tower lamp" in text or "tower light" in text:
        light_id = 13

    if light_id_2 == 0:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        requests.put(url, data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
    else:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        url2 = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id_2) + "/state/"
        requests.put(url, data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))
        requests.put(url2, data=json.dumps(LIGHT_PAYLOADS['concentrate_payload']))


def turn_off_light(text):
    light_id = 0
    light_id_2 = 0
    if "bedroom lamp" in text or "bedroom light" in text:
        light_id = 1
    if "mirror light" in text or "mirror lamp" in text:
        light_id = 5
    if "ceiling light" in text:
        light_id = 7
        light_id_2 = 8
    if "studio light" in text or "studio lamp" in text or "office light" in text or "office lamp" in text:
        light_id = 9
    if "tv lights" in text:
        light_id = 10
        light_id_2 = 11
    if "table lamp" in text or "table light" in text or "living room lamp" in text or "living room light" in text:
        light_id = 12
    if "tower lamp" in text or "tower light" in text:
        light_id = 13

    if light_id_2 == 0:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        requests.put(url, data=json.dumps(LIGHT_PAYLOADS['off_payload']))
    else:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        url2 = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id_2) + "/state/"
        requests.put(url, data=json.dumps(LIGHT_PAYLOADS['off_payload']))
        requests.put(url2, data=json.dumps(LIGHT_PAYLOADS['off_payload']))


def time_to_sound(time):
    if time == "00:00:00":
        return TIME_SOUNDS['s_zero']
    if time == "01:00:00":
        return TIME_SOUNDS['s_one']
    if time == "02:00:00":
        return TIME_SOUNDS['s_two']
    if time == "03:00:00":
        return TIME_SOUNDS['s_three']
    if time == "04:00:00":
        return TIME_SOUNDS['s_four']
    if time == "05:00:00":
        return TIME_SOUNDS['s_five']
    if time == "06:00:00":
        return TIME_SOUNDS['s_six']
    if time == "07:00:00":
        return TIME_SOUNDS['s_seven']
    if time == "08:00:00":
        return TIME_SOUNDS['s_eight']
    if time == "09:00:00":
        return TIME_SOUNDS['s_nine']
    if time == "10:00:00":
        return TIME_SOUNDS['s_ten']
    if time == "11:00:00":
        return TIME_SOUNDS['s_oneone']
    if time == "12:00:00":
        return TIME_SOUNDS['s_onetwo']
    if time == "13:00:00":
        return TIME_SOUNDS['s_onethree']
    if time == "14:00:00":
        return TIME_SOUNDS['s_onefour']
    if time == "15:00:00":
        return TIME_SOUNDS['s_onefive']
    if time == "16:00:00":
        return TIME_SOUNDS['s_onesix']
    if time == "17:00:00":
        return TIME_SOUNDS['s_oneseven']
    if time == "18:00:00":
        return TIME_SOUNDS['s_oneeight']
    if time == "19:00:00":
        return TIME_SOUNDS['s_onenine']
    if time == "20:00:00":
        return TIME_SOUNDS['s_twozero']
    if time == "21:00:00":
        return TIME_SOUNDS['s_twoone']
    if time == "22:00:00":
        return TIME_SOUNDS['s_twotwo']
    if time == "23:00:00":
        return TIME_SOUNDS['s_twothree']


def turnoff_outlet():
    os.system('sthelper turnoff "M.O.R.G. Light"')


def turnon_outlet():
    os.system('sthelper turnon "M.O.R.G. Light"')

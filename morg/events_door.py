import datetime as dt
import json
import os
import random
import re
import sys
import time

import requests

from constants import SOUNDS
from events_text import send_text
from events_weather import weather_update
from logger import morg_log
from utils import (bright_lights_on, concentrate_lights_on, dim_lights_on,
                   morning_lights_on, play_sound, play_weather_report_sound,
                   turnoff_outlet, turnon_outlet)

PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/18'
SWITCH_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/4'


# -----------------------
def get_motion_state():
    """
    Get front door motion state
    :return: bool(True or False)
    """
    try:
        response = requests.get(PIR_URL)
        json_data = json.loads(response.text)
        return json_data['state']['presence'] is True
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        return False


# -----------------------
def get_switch_state():
    """
    Get button switch state
    :return: str(inside or outside)
    """
    try:
        response = requests.get(SWITCH_URL)
        json_data = json.loads(response.text)
        state = json_data['state']['buttonevent']
        if 1000 <= state <= 1010:
            return "inside"
        if 2000 <= state <= 2010:
            return "inside"
        if 3000 <= state <= 3010:
            return "outside"
        if 4000 <= state <= 4010:
            return "outside"
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        return "outside"


# -----------------------
def grab_last_motion_line():
    """
    Get the last motion trigger from MORG.log
    :return: datetime(last_motion)
    """
    try:
        line_count = 0
        fname = "/Users/kuchambers/PycharmProjects/M.O.R.G./logs/MORG.log"
        with open(fname, 'r') as f:
            for _ in f:
                line_count += 1

        log_file = open(fname, "r")
        lines = log_file.readlines()
        log_file.close()

        line_count_end_range = line_count - 101
        line_count = line_count - 1
        while line_count >= line_count_end_range:
            if "lastmotion:" in lines[line_count]:
                last_line = lines[line_count]
                last_line = last_line.rstrip()
                last_chars = last_line[-28:]
                last_chars = re.sub('\| ', '', last_chars)
                last_motion = dt.datetime.strptime(last_chars, '%Y-%m-%d %H:%M:%S.%f')
                return last_motion
            line_count = line_count - 1
        return False
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/morg.pid")
        sys.exit()


# -----------------------
def check_for_inside():
    """
    Check for the word "inside" in the MORG.log
    :return: bool(ready)
    """
    linecount = 0
    fname = "/Users/kuchambers/PycharmProjects/M.O.R.G./logs/MORG.log"
    with open(fname, 'r') as f:
        for line in f:
            linecount += 1

    linetoread1 = linecount - 200
    linetoread2 = linecount - 201
    linetoread3 = linecount - 202

    a_file = open("/Users/kuchambers/PycharmProjects/M.O.R.G./logs/MORG.log")
    lines_to_read = [linetoread1,
                     linetoread2,
                     linetoread3]

    for position, line in enumerate(a_file):
        if position in lines_to_read:
            if "inside" in line:
                print("Found the word inside")
                time.sleep(60.0)
                return False
    return True




### MORNING ACTIONS
def morning_short_trigger():
    """
    Trigger actions for morning 10min - 40min
    """
    send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_welcomeback_g'])
    morning_lights_on()
    time.sleep(1.0)
    play_sound(SOUNDS['s_lightson'])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()

def morning_medium_trigger():
    """
    Trigger actions for morning 40min - 150min
    """
    send_text('Front door has been opened.\n\nGood morning sir.\n\n-M.O.R.G.')

    morning_phrases = ["s_morningwelcomeback1",
                       "s_morningwelcomeback2"]

    rint = 0
    rint = random.randint(0, 1)
    path = morning_phrases[rint]

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_welcomeback_g'])
    morning_lights_on()
    play_sound(SOUNDS['s_lightson'])
    play_weather_report_sound()
    weather_update()
    time.sleep(1.0)
    play_sound(SOUNDS[path])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()

def morning_long_trigger():
    """
    Trigger actions for morning > 150min
    """
    send_text('Front door has been opened.\n\nGood morning sir.\n\n-M.O.R.G.')

    morning_phrases = ["s_morninghadfun",
                       "s_morningproductive"]

    rint = 0
    rint = random.randint(0, 1)
    path = morning_phrases[rint]

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_goodmorning_g'])
    morning_lights_on()
    play_sound(SOUNDS['s_lightson'])
    play_weather_report_sound()
    weather_update()
    time.sleep(1.0)
    play_sound(SOUNDS[path])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()


### AFTERNOON ACTIONS
def afternoon_short_trigger():
    """
    Trigger actions for afternoon 10min - 40min
    """
    send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_welcomeback_g'])
    concentrate_lights_on()
    time.sleep(1.0)
    play_sound(SOUNDS['s_lightson'])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()

def afternoon_medium_trigger():
    """
    Trigger actions for afternoon 40min - 150min
    """
    send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

    afternoon_phrases = ["s_afternoonwelcomeback1",
                         "s_afternoonwelcomeback2",
                         "s_anyplans"]

    rint = 0
    rint = random.randint(0, 1)
    path = afternoon_phrases[rint]

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_welcomemrchambers_g'])
    concentrate_lights_on()
    time.sleep(1.0)
    play_sound(SOUNDS[path])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()

def afternoon_long_trigger(weekday):
    """
    Trigger actions for afternoon > 150min
    :param weekday: datetime.weekday()
    """
    afternoon_text_phrases = ["Good afternoon sir.",
                              "Hope you're having a wonderful afternoon."]
    rint = 0
    rint = random.randint(0, 1)
    text_phrase = afternoon_text_phrases[rint]
    send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')
    if weekday == 4:  # longer than 150min, is it friday?

        friday_afternoon_phrases = ["s_sevensummers",
                                    "s_withoutyou",
                                    "s_allyourn",
                                    "s_watermelonsugar",
                                    "s_freebird"]

        rint = 0
        rint = random.randint(0, 1)
        path = friday_afternoon_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodafternoon_g'])
        concentrate_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS['s_fridayhowsmusic_m'])
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()
    elif weekday == 5:  # longer than 150min, is it saturday?

        saturday_phrases = ["s_saturdaybackinblack_m",
                            "s_saturdayhighwaytohell_m"]

        rint = 0
        rint = random.randint(0, 1)
        path = saturday_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodafternoon_g'])
        concentrate_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()
    else:  # longer than 150min

        afternoon_phrases = ["s_sevensummers",
                             "s_withoutyou",
                             "s_allyourn",
                             "s_watermelonsugar",
                             "s_freebird"]

        rint = 0
        rint = random.randint(0, 4)
        path = afternoon_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodafternoon_g'])
        concentrate_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS['s_productiveday_m'])
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()


### EVENING ACTIONS
def evening_short_trigger():
    """
    Trigger actions for evening 10min - 40min
    """
    evening_text_phrases = ["Good evening sir.",
                            "Make the most of your evening sir."]
    rint = 0
    rint = random.randint(0, 1)
    text_phrase = evening_text_phrases[rint]
    send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_welcomeback_g'])
    bright_lights_on()
    time.sleep(1.0)
    play_sound(SOUNDS['s_lightson'])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()


def evening_medium_trigger(weekday):
    """
    Trigger actions for evening 40min - 150min
    :param weekday: datetime.weekday()
    """
    evening_text_phrases = ["Good evening sir.",
                            "Make the most of your evening sir."]
    rint = 0
    rint = random.randint(0, 1)
    text_phrase = evening_text_phrases[rint]
    send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

    if 4 <= weekday <= 5:  # between friday - saturday
        evening_back_weekend_phrases = ["s_anycompany",
                                        "s_anyplans"]
        rint = 0
        rint = random.randint(0, 1)
        path = evening_back_weekend_phrases[rint]

        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodevening_g'])
        bright_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()
    else:
        evening_phrases = ["s_howwasyourafternoon",
                           "s_eveningwelcomeback1",
                           "s_eveningwelcomeback2"]

        rint = 0
        rint = random.randint(0, 1)
        path = evening_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_welcomeback_g'])
        bright_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()

def evening_long_trigger(weekday):
    """
    Trigger actions for evening > 150min
    :param weekday: datetime.weekday()
    """
    evening_text_phrases = ["Good evening sir.",
                            "Make the most of your evening sir."]
    rint = 0
    rint = random.randint(0, 1)
    text_phrase = evening_text_phrases[rint]
    send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

    if weekday == 4:  # is it friday?
        evening_phrases = ["s_toosieslide",
                           "s_whatspoppin",
                           "s_wayout",
                           "s_up"]
        rint = 0
        rint = random.randint(0, 3)
        path = evening_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodevening_g'])
        bright_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS['s_fridayheresmusic_m'])
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()
    if weekday == 5:  # is it saturday?
        evening_phrases = ["s_toosieslide",
                           "s_whatspoppin",
                           "s_wayout",
                           "s_up"]
        rint = 0
        rint = random.randint(0, 3)
        path = evening_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodevening_g'])
        bright_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS['s_saturdaysequence_m'])
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()
    if 0 <= weekday <= 3 or weekday == 6:  # between sunday - thursday
        evening_phrases = ["s_withoutyou",
                           "s_allyourn",
                           "s_watermelonsugar",
                           "s_sevensummers", ]
        rint = 0
        rint = random.randint(0, 3)
        path = evening_phrases[rint]

        turnon_outlet()
        time.sleep(1.0)
        play_sound(SOUNDS['s_wake'])
        play_sound(SOUNDS['s_goodevening_g'])
        bright_lights_on()
        time.sleep(1.0)
        play_sound(SOUNDS['s_howssomemusic_m'])
        play_sound(SOUNDS[path])
        time.sleep(0.5)
        play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
        turnoff_outlet()


### LATENIGHT ACTIONS
def latenight_trigger(weekday):
    """
    Trigger actions for latenight > 60min
    :param weekday: datetime.weekday()
    """
    if 4 <= weekday <= 6:
        send_text('Front door has been opened.\n\nEnjoy your late night sir.\n\n-M.O.R.G.')

    if 0 <= weekday <= 3:
        send_text(
            'Front door has been opened.\n\nLate night I see? Get some rest for the morning '
            'sir.\n\n-M.O.R.G.')

    turnon_outlet()
    time.sleep(1.0)
    play_sound(SOUNDS['s_wake'])
    play_sound(SOUNDS['s_dimlight'])
    dim_lights_on()
    time.sleep(1.0)
    play_sound(SOUNDS['s_lightson'])
    play_sound(SOUNDS['s_welcomeback_g'])
    time.sleep(0.5)
    play_sound("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/listen_stop.wav")
    turnoff_outlet()

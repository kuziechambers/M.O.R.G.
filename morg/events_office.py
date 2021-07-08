import datetime as dt
import json
import os
import random
import re
import sys
import time

import requests

from constants import SOUNDS, TIME_FRAMES
from events_text import send_text
from events_weather import weather_update
from logger import morg_log
from utils import (morning_lights_on, play_sound, play_weather_report_sound,
                   turnoff_outlet, turnon_outlet)

OFFICE_PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/39'

def get_office_motion_state():
    try:
        response = requests.get(OFFICE_PIR_URL)
        json_data = json.loads(response.text)
        return json_data['state']['presence']
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        try:
            os.remove("/tmp/morg.pid")
        except FileNotFoundError as e:
            e = sys.exc_info()
            send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
            morg_log.error(str(e))
        return False


def check_for_recent_trigger():
    """
    Check for the line "GREETING TRIGGERED" in the MORG.log
    :return: bool
    """
    try:
        linecount = 0
        fname = "/home/pi/M.O.R.G./logs/MORG.log"
        with open(fname, 'r') as f:
            for line in f:
                linecount += 1
            f.close()

        lines_to_read = []
        count = 1
        while count <= 200:
            linetoread = linecount - count
            lines_to_read.append(linetoread)
            count = count + 1
        a_file = open("/home/pi/M.O.R.G./logs/MORG.log")
        for position, line in enumerate(a_file):
            if position in lines_to_read:
                if "DOOR GREETING TRIGGERED" in line:
                    print("Found the word TRIGGERED")
                    a_file.close()
                    return False
        a_file.close()
        return True
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        try:
            os.remove("/tmp/morg.pid")
        except FileNotFoundError as e:
            e = sys.exc_info()
            send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
            morg_log.error(str(e))
        sys.exit()


# -----------------------
def since_office_motion_init():
    try:
        response = requests.get(OFFICE_PIR_URL)
        json_data = json.loads(response.text)
        last_motion_update = json_data['state']['lastupdated']
        pattern = r'T'
        last_motion_update = re.sub(pattern, ' ', last_motion_update)
        last_motion_update = dt.datetime.strptime(last_motion_update, '%Y-%m-%d %H:%M:%S')
        last_motion_update = last_motion_update - dt.timedelta(hours=5)

        file = open("/home/pi/M.O.R.G./logs/office_motion.log", "w+")
        file.write(str(last_motion_update))
        file.close()
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        try:
            os.remove("/tmp/morg.pid")
        except FileNotFoundError as e:
            e = sys.exc_info()
            send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
            morg_log.error(str(e))
        sys.exit()


# -----------------------
def since_office_motion_update():
    try:
        response = requests.get(OFFICE_PIR_URL)
        json_data = json.loads(response.text)
        last_motion_update = json_data['state']['lastupdated']
        pattern = r'T'
        last_motion_update = re.sub(pattern, ' ', last_motion_update)
        last_motion_update = dt.datetime.strptime(last_motion_update, '%Y-%m-%d %H:%M:%S')
        last_motion_update = last_motion_update - dt.timedelta(hours=5)

        a_file = open("/home/pi/M.O.R.G./logs/office_motion.log", "r")
        line = a_file.read()
        a_file.close()

        if str(last_motion_update) != line:
            line = dt.datetime.strptime(line, '%Y-%m-%d %H:%M:%S')
            seconds_away = (last_motion_update - line).total_seconds()
            if seconds_away > 9000 and TIME_FRAMES['morning_start_office'] <= last_motion_update.time() <= TIME_FRAMES['morning_end_office']:
                if check_for_recent_trigger() is True:
                    morg_log.info("Office state: " + str(get_office_motion_state()) + "  | difference between " + str(line) + " and " + str(last_motion_update) + " was: " + str(seconds_away))
                    morg_log.info("OFFICE GREETING TRIGGERED")
                    file = open("/home/pi/M.O.R.G./logs/office_motion.log", "w+")
                    file.write(str(last_motion_update))
                    file.close()

                    weekday = dt.datetime.now().weekday()

                    if weekday == 0:
                        turnon_outlet()
                        time.sleep(1.0)
                        play_sound(SOUNDS['s_wake'])
                        play_sound(SOUNDS['s_goodmorning_g'])
                        morning_lights_on()
                        play_sound(SOUNDS['s_lightson'])
                        play_weather_report_sound()
                        weather_update()
                        time.sleep(1.0)
                        play_sound(SOUNDS['s_mondaymorning'])
                        time.sleep(0.5)
                        play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
                        turnoff_outlet()

                    if weekday == 1:
                        phrases = ["s_tuesdaymorning",
                                   "s_morningproductive"]

                        rint = 0
                        rint = random.randint(0, 1)
                        path = phrases[rint]

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
                        play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
                        turnoff_outlet()

                    if weekday == 2:
                        phrases = ["s_wednesdaymorning",
                                   "s_morningsleptwell"]

                        rint = 0
                        rint = random.randint(0, 1)
                        path = phrases[rint]

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
                        play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
                        turnoff_outlet()

                    if weekday == 3:
                        phrases = ["s_thursdaymorning",
                                   "s_morninggreatday"]

                        rint = 0
                        rint = random.randint(0, 1)
                        path = phrases[rint]

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
                        play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
                        turnoff_outlet()

                    if weekday == 4:
                        turnon_outlet()
                        time.sleep(1.0)
                        play_sound(SOUNDS['s_wake'])
                        play_sound(SOUNDS['s_goodmorning_g'])
                        morning_lights_on()
                        play_sound(SOUNDS['s_lightson'])
                        play_weather_report_sound()
                        weather_update()
                        time.sleep(1.0)
                        play_sound(SOUNDS['s_fridaymorning'])
                        time.sleep(0.5)
                        play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
                        turnoff_outlet()

    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        try:
            os.remove("/tmp/morg.pid")
        except FileNotFoundError as e:
            e = sys.exc_info()
            send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
            morg_log.error(str(e))
        sys.exit()

import json
import requests
import sys
import re
import datetime as dt
from text_service import send_text
from smartthings import *
from constants_sound import *
from constants_time import *


PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/18'
OFFICE_PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/39'
SWITCH_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/4'


# -----------------------
def get_motion_state():
    try:
        response = requests.get(PIR_URL)
        json_data = json.loads(response.text)
        return json_data['state']['presence'] is True
    except:
        e = sys.exc_info()
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')

        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write(str(e))
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.close()
        return False


# -----------------------
def get_switch_state():
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
        e = sys.exc_info()
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')

        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write(str(e))
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.close()
        return "outside"


# -----------------------
def get_office_motion_state():
    try:
        response = requests.get(OFFICE_PIR_URL)
        json_data = json.loads(response.text)
        return json_data['state']['presence']
    except:
        e = sys.exc_info()
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')

        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write(str(e))
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.close()
        return False


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
        e = sys.exc_info()
        print(e)
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')

        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write(str(e))
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.close()


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
            if seconds_away > 5400 and morning_start_away <= last_motion_update.time() <= morning_end_away:
                log = open("/home/pi/M.O.R.G./logs/MORG.log", "a+")
                log.write("Office state: " + str(get_office_motion_state()) + "  | difference between " + str(line) + " and " + str(last_motion_update) + " was: " + str(seconds_away))
                log.write("\n")
                log.close()

                turnon_outlet()
                play_sound(s_wake2)
                play_sound(s_brightlightseq)
                bright_lights_on()
                play_sound(s_sequencecomplete)
                play_sound(s_onlygoodmorning)
                turnoff_outlet()

                file = open("/home/pi/M.O.R.G./logs/office_motion.log", "w+")
                file.write(str(last_motion_update))
                file.close()
    except:
        e = sys.exc_info()
        print(e)
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')

        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.write(str(e))
        logfile.write("\n")
        logfile.write("\n")
        logfile.write("\n")
        logfile.close()


# -----------------------
def grab_last_motion_line():
    lcount = 0
    fname = "/home/pi/M.O.R.G./logs/MORG.log"
    with open(fname, 'r') as f:
        for _ in f:
            lcount += 1

    l_file = open(fname, "r")
    l_lines = l_file.readlines()
    l_file.close()

    lcount = lcount - 15
    lastline = l_lines[lcount]
    lastline = lastline.rstrip()

    last_chars = lastline[-28:]
    last_chars = re.sub('\| ', '', last_chars)
    last_motion = dt.datetime.strptime(last_chars, '%Y-%m-%d %H:%M:%S.%f')
    return last_motion


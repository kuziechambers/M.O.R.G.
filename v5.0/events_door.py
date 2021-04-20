import sys
import re
import datetime as dt
import requests
import json
import os
from events_text import send_text
from logger import morg_log


PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/18'
SWITCH_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/4'


# -----------------------
def get_motion_state():
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
    try:
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
    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/mydaemon.pid")
        exit()


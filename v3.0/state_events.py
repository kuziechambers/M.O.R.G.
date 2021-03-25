import json
import requests
import sys
import re
import time
import datetime as dt
from datetime import time as ti
from text_service import send_text



PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/18'
SWITCH_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/4'

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
    
    
def grab_last_motion_line():
    lcount = 0
    fname = "/home/pi/M.O.R.G./logs/MORG.log"
    with open(fname, 'r') as f:
        for line in f:
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


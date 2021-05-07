import sys
import re
import datetime as dt
import random
import time
from events_text import send_text
from constants import *
from logger import morg_log
from events_weather import weather_update

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
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/morg.pid")
        exit()


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
            if seconds_away > 9000 and morning_start_office <= last_motion_update.time() <= morning_end_office:
                morg_log.info("Office state: " + str(get_office_motion_state()) + "  | difference between " + str(line) + " and " + str(last_motion_update) + " was: " + str(seconds_away))
                file = open("/home/pi/M.O.R.G./logs/office_motion.log", "w+")
                file.write(str(last_motion_update))
                file.close()

                weekday = dt.datetime.now().weekday()

                if weekday == 0:
                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    play_sound(sounds['s_goodmorning_g'])
                    morning_lights_on()
                    play_sound(sounds['s_lightson'])
                    weather_update()
                    time.sleep(1.0)
                    play_sound(sounds['s_mondaymorning'])
                    turnoff_outlet()

                if weekday == 1:
                    phrases = ["s_tuesdaymorning",
                               "s_morningproductive"]

                    rint = 0
                    rint = random.randint(0, 1)
                    path = phrases[rint]

                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    play_sound(sounds['s_goodmorning_g'])
                    morning_lights_on()
                    play_sound(sounds['s_lightson'])
                    weather_update()
                    time.sleep(1.0)
                    play_sound(sounds[path])
                    turnoff_outlet()

                if weekday == 2:
                    phrases = ["s_wednesdaymorning",
                               "s_morningsleptwell"]

                    rint = 0
                    rint = random.randint(0, 1)
                    path = phrases[rint]

                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    play_sound(sounds['s_goodmorning_g'])
                    morning_lights_on()
                    play_sound(sounds['s_lightson'])
                    weather_update()
                    time.sleep(1.0)
                    play_sound(sounds[path])
                    turnoff_outlet()

                if weekday == 3:
                    phrases = ["s_thursdaymorning",
                               "s_morninggreatday"]

                    rint = 0
                    rint = random.randint(0, 1)
                    path = phrases[rint]

                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    play_sound(sounds['s_goodmorning_g'])
                    morning_lights_on()
                    play_sound(sounds['s_lightson'])
                    weather_update()
                    time.sleep(1.0)
                    play_sound(sounds[path])
                    turnoff_outlet()

                if weekday == 4:
                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    play_sound(sounds['s_goodmorning_g'])
                    morning_lights_on()
                    play_sound(sounds['s_lightson'])
                    weather_update()
                    time.sleep(1.0)
                    play_sound(sounds['s_fridaymorning'])
                    turnoff_outlet()

    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/morg.pid")
        exit()

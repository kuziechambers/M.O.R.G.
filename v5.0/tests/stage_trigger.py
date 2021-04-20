import datetime as dt
import sys
import time
from door_events import (
    get_motion_state
)
from smartthings import turnon_outlet, turnoff_outlet
from constants_sound import sounds, play_sound, concentrate_lights_on
from constants_time import *
from weather_events import weather_update



stage_time = "2021-03-01 12:00:00.000000"

last_motion = dt.datetime.strptime(stage_time, '%Y-%m-%d %H:%M:%S.%f')

while True:
    try:
        # Get sensor states
        motion = get_motion_state()

        # Get time values
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        last_motion_date = last_motion.date()
        last_motion_time = last_motion.time()
        seconds_away = (now - last_motion).total_seconds()
        weekday = dt.datetime.now().weekday()

        if motion is True:
            if seconds_away > 3600:
                # turnon_outlet()
                # time.sleep(1.0)
                # play_sound(sounds['s_wake'])
                # play_sound(sounds['s_welcomeback_g'])
                # bright_lights_on()
                # time.sleep(1.0)
                # play_sound(sounds['s_eveningwelcomeback2'])
                # #play_sound(sounds['s_up'])
                # turnoff_outlet()

                turnon_outlet()
                time.sleep(1.0)
                play_sound(sounds['s_wake'])
                play_sound(sounds['s_goodmorning_g'])
                concentrate_lights_on()
                play_sound(sounds['s_lightson'])
                weather_update()
                time.sleep(1.0)
                play_sound(sounds['s_mondaymorning'])
                turnoff_outlet()
    except:
        ex = sys.exc_info()
        print(ex)
        exit()







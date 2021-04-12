import datetime as dt
import os
import random
import sys
import time
from door_events import (
    get_motion_state,
    get_switch_state,
    grab_last_motion_line
    )
from office_events import (
    since_office_motion_init,
    since_office_motion_update,
)
from smartthings import turnon_outlet, turnoff_outlet
from constants_sound import sounds, play_sound, bright_lights_on, concentrate_lights_on
from constants_time import *
from message_service import send_text
from weather_events import weather_update



stage_time = "2021-03-01 12:00:00.000000"

last_motion = dt.datetime.strptime(stage_time, '%Y-%m-%d %H:%M:%S.%f')

while True:
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
            time.sleep(1.0)
            play_sound(sounds['s_mondaymorning'])
            turnoff_outlet()
            weather_update()






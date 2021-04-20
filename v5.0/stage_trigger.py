import random
from events_door import (
    get_motion_state
)
import sys
import datetime as dt
import time
from constants import turnon_outlet, turnoff_outlet, play_sound, sounds, concentrate_lights_on
from events_weather import weather_update



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

                phrases = ["s_tuesdaymorning",
                           "s_morningproductive"]

                rint = 0
                rint = random.randint(0, 1)
                path = phrases[rint]

                turnon_outlet()
                time.sleep(1.0)
                play_sound(sounds['s_wake'])
                play_sound(sounds['s_goodmorning_g'])
                concentrate_lights_on()
                play_sound(sounds['s_lightson'])
                weather_update()
                time.sleep(1.0)
                play_sound(sounds[path])
                turnoff_outlet()
    except KeyboardInterrupt:
        exit()
    except:
        ex = sys.exc_info()
        print(ex)
        exit()







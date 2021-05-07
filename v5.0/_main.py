import datetime as dt
import random
import sys
import time
from events_door import (
    get_motion_state, get_switch_state, grab_last_motion_line, check_for_inside,
    morning_short_trigger, morning_medium_trigger, morning_long_trigger,
    afternoon_short_trigger, afternoon_medium_trigger, afternoon_long_trigger,
    evening_short_trigger, evening_medium_trigger, evening_long_trigger,
    latenight_trigger
    )
from events_office import (
    since_office_motion_init,
    since_office_motion_update,
)
from events_ibm import tts_transcribe_play
from events_sports import get_mavs_game
from constants import *
from events_text import send_text
from events_weather import weather_update, weekend_weather_update, get_weekend_temp


# Grab and write pid to .pid file
pid = str(os.getpid())
pidfile = "/tmp/morg.pid"
logfile = open(pidfile, "w").write(pid)

# Send startup text
send_text('Script booted sir.\n\n-M.O.R.G.')
print("Script booted sir.")

# Import morg_log logger
from logger import morg_log

# Initiate last_motion times
last_motion = grab_last_motion_line()
since_office_motion_init()


while True:
    try:
        # Get sensor states
        motion = get_motion_state()
        switch = get_switch_state()

        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        last_motion_date = last_motion.date()
        last_motion_time = last_motion.time()
        seconds_away = (now - last_motion).total_seconds()
        weekday = dt.datetime.now().weekday()

        # Log constantly
        morg_log.info(str(now_date) +
                      " | " +
                      str(now_time) +
                      " ----- motionstatus: "
                      + str(motion) + ",  switchstatus: " + str(switch) + ",  secondsaway: " + str(seconds_away) +
                      ",  lastmotion: " + str(last_motion_date) + " | " + str(last_motion_time))


        ####################
        ###### Inside ######
        ####################
        if switch == "inside":
            if motion is False:  # Inside - False
                if 0 <= weekday <= 4:
                    since_office_motion_update()
                time.sleep(2.0)
                if weekday == 4 and weekend_start <= now_time <= weekend_end: # Weekend-start
                    temps = get_weekend_temp()
                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    weekend_weather_update(temps)
                    turnoff_outlet()
                if weekend_start <= now_time <= weekend_end: # Get Mavs game
                    true_or_false, text = get_mavs_game()
                    if true_or_false:
                        play_sound("/home/pi/M.O.R.G./stt_files/speak.wav")
                        tts_transcribe_play(text)

            if motion is True:  # Inside - True
                last_motion = dt.datetime.now()
                time.sleep(30.0)


        #####################
        ###### Outside ######
        #####################
        if switch == "outside":
            if motion is False:  # Outside - False
                play_sound(sounds['s_ping'])

                if 36000 < seconds_away < 36007 and morning_start_away <= now_time <= morning_end_away:
                    send_text('Good morning sir.\nI slept quite well last night without your being here.\n\n-M.O.R.G.')

                if 115200 < seconds_away < 115207 and afternoon_start_away <= now_time <= afternoon_end_away:
                    send_text('Greetings Mr.Chambers,\nI hope you are having a wonderful time away sir.\n\n-M.O.R.G.')

                if 14400 < seconds_away < 14407 and evening_start_away <= now_time <= evening_end_away:
                    send_text('Good evening sir,\nEnjoying your night I hope.\n\n-M.O.R.G.')

            if motion is True:  # Outside - True
                last_motion = dt.datetime.now()
                ready = check_for_inside()

                if ready is True:  # Time to trigger greeting
                    turnon_outlet()

                    if morning_start <= now_time <= morning_end:  # MORNING
                        if 600 < seconds_away < 2400:  # between 10min - 40min
                            morning_short_trigger()

                        if 2400 < seconds_away < 9000:  # between 40min - 150min
                            morning_medium_trigger()

                        if seconds_away > 9000:  # longer than 150min
                            morning_long_trigger()


                    elif afternoon_start <= now_time <= afternoon_end:  # AFTERNOON
                        if 600 < seconds_away < 2400:  # between 10min - 40min
                            afternoon_short_trigger()

                        if 2400 < seconds_away < 9000:  # between 40min - 150min
                            afternoon_medium_trigger()

                        elif seconds_away > 9000:  # longer than 150min
                            afternoon_long_trigger(weekday)


                    elif evening_start <= now_time <= evening_end:  # EVENING
                        evening_text_phrases = ["Good evening sir.",
                                                "Make the most of your evening sir."]
                        rint = 0
                        rint = random.randint(0, 1)
                        text_phrase = evening_text_phrases[rint]
                        send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

                        if 600 < seconds_away < 2400:  # between 10min - 40min
                            evening_short_trigger()

                        if 2400 < seconds_away < 9000:  # between 40min - 150min
                            evening_medium_trigger(weekday)

                        if seconds_away > 9000:  # longer than 150min
                            evening_long_trigger(weekday)


                    elif latenight_start <= now_time <= latenight_end:  # LATE NIGHT
                        if seconds_away > 3600:  # longer than 60min
                            latenight_trigger(weekday)

                    time.sleep(420.0)

    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/morg.pid")

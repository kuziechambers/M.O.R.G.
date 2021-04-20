import datetime as dt
import random
import sys
import time
from events_door import (
    get_motion_state,
    get_switch_state,
    grab_last_motion_line
    )
from events_office import (
    since_office_motion_init,
    since_office_motion_update,
)
from constants import *
from events_text import send_text
from events_weather import weather_update, weekend_weather_update, get_weekend_temp


# Grab and write pid to .pid file
pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"
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
        #seconds_away = 10000
        weekday = dt.datetime.now().weekday()

        # Log constantly
        morg_log.info(str(now_date) +
                      " | " +
                      str(now_time) +
                      " ----- motionstatus: "
                      + str(motion) + ",  switchstatus: " + str(switch) + ",  secondsaway: " + str(seconds_away) +
                      ",  lastmotion: " + str(last_motion_date) + " | " + str(last_motion_time))

        # Inside
        if switch == "inside":
            if motion is False:  # Inside - False
                if 0 <= weekday <= 4:
                    since_office_motion_update()
                time.sleep(2.0)
                if weekday == 4 and weekend_start <= now_time <= weekend_end:
                    temps = get_weekend_temp()
                    turnon_outlet()
                    time.sleep(1.0)
                    play_sound(sounds['s_wake'])
                    weekend_weather_update(temps)
                    turnoff_outlet()

            if motion is True:  # Inside - True
                last_motion = dt.datetime.now()
                time.sleep(30.0)

        # Outside
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

                linecount = 0
                fname = "/home/pi/M.O.R.G./logs/MORG.log"
                with open(fname, 'r') as f:
                    for line in f:
                        linecount += 1

                linetoread1 = linecount - 200
                linetoread2 = linecount - 201
                linetoread3 = linecount - 202

                a_file = open("/home/pi/M.O.R.G./logs/MORG.log")
                lines_to_read = [linetoread1,
                                 linetoread2,
                                 linetoread3]

                ready = True
                for position, line in enumerate(a_file):
                    if position in lines_to_read:
                        if "inside" in line:
                            print("Found the word inside")
                            ready = False
                            time.sleep(60.0)
                            break

                if ready is True:  # Time to trigger greeting

                    turnon_outlet()

                    if morning_start <= now_time <= morning_end:  # MORNING

                        if 600 < seconds_away < 2400:  # between 10min - 40min

                            send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_welcomeback_g'])
                            concentrate_lights_on()
                            time.sleep(1.0)
                            play_sound(sounds['s_lightson'])
                            turnoff_outlet()

                        if 2400 < seconds_away < 7200:  # between 40min - 120min

                            send_text('Front door has been opened.\n\nGood morning sir.\n\n-M.O.R.G.')

                            morning_phrases = ["s_morningwelcomeback1",
                                               "s_morningwelcomeback2"]

                            rint = 0
                            rint = random.randint(0, 1)
                            path = morning_phrases[rint]

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_welcomeback_g'])
                            concentrate_lights_on()
                            play_sound(sounds['s_lightson'])
                            weather_update()
                            time.sleep(1.0)
                            play_sound(sounds[path])
                            turnoff_outlet()

                        if seconds_away > 7200:  # longer than 120min

                            send_text('Front door has been opened.\n\nGood morning sir.\n\n-M.O.R.G.')

                            morning_phrases = ["s_morninghadfun",
                                               "s_morningproductiveday"]

                            rint = 0
                            rint = random.randint(0, 1)
                            path = morning_phrases[rint]

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_goodmorning_g'])
                            concentrate_lights_on()
                            play_sound(sounds['s_lightson'])
                            weather_update()
                            time.sleep(1.0)
                            play_sound(sounds[path])
                            turnoff_outlet()

                    elif afternoon_start <= now_time <= afternoon_end:  # AFTERNOON

                        if 600 < seconds_away < 2400:  # between 10min - 40min

                            send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_welcomeback_g'])
                            concentrate_lights_on()
                            time.sleep(1.0)
                            play_sound(sounds['s_lightson'])
                            turnoff_outlet()

                        if 2400 < seconds_away < 7200:  # between 40min - 120min

                            send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')

                            afternoon_phrases = ["s_afternoonwelcomeback1",
                                                 "s_afternoonwelcomeback2,"
                                                 "s_anyplans"]

                            rint = 0
                            rint = random.randint(0, 1)
                            path = afternoon_phrases[rint]

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_welcomemrchambers_g'])
                            concentrate_lights_on()
                            time.sleep(1.0)
                            play_sound(sounds[path])
                            turnoff_outlet()

                        elif seconds_away > 7200:  # longer than 120min
                            afternoon_text_phrases = ["Good afternoon sir.",
                                                      "Hope you're having a wonderful afternoon."]
                            rint = 0
                            rint = random.randint(0, 1)
                            text_phrase = afternoon_text_phrases[rint]
                            send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

                            if weekday == 4:  # longer than 120min, is it friday?

                                friday_afternoon_phrases = ["s_sevensummers",
                                                            "s_withoutyou",
                                                            "s_allyourn",
                                                            "s_watermelonsugar",
                                                            "s_freebird"]

                                rint = 0
                                rint = random.randint(0, 1)
                                path = friday_afternoon_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodafternoon_g'])
                                concentrate_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_fridayhowsmusic_m'])
                                play_sound(sounds[path])
                                turnoff_outlet()

                            elif weekday == 5:  # longer than 120min, is it saturday?

                                saturday_phrases = ["s_saturdaybackinblack_m",
                                                    "s_saturdayhighwaytohell_m"]

                                rint = 0
                                rint = random.randint(0, 1)
                                path = saturday_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodafternoon_g'])
                                concentrate_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds[path])
                                turnoff_outlet()


                            else:  # longer than 120min

                                afternoon_phrases = ["s_sevensummers",
                                                     "s_withoutyou",
                                                     "s_allyourn",
                                                     "s_watermelonsugar",
                                                     "s_freebird"]

                                rint = 0
                                rint = random.randint(0, 4)
                                path = afternoon_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodafternoon_g'])
                                concentrate_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_productiveday_m'])
                                play_sound(sounds[path])
                                turnoff_outlet()

                    elif evening_start <= now_time <= evening_end:  # EVENING

                        evening_text_phrases = ["Good evening sir.",
                                                "Make the most of your evening sir."]
                        rint = 0
                        rint = random.randint(0, 1)
                        text_phrase = evening_text_phrases[rint]
                        send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')

                        if 600 < seconds_away < 2400:  # between 10min - 40min

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_welcomeback_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_lightson'])
                                turnoff_outlet()

                        if 2400 < seconds_away < 7200:  # between 40min - 120min

                            if 4 <= weekday <= 5:  # between friday - saturday

                                evening_back_weekend_phrases = ["s_anycompany",
                                                                "s_anyplans"]

                                rint = 0
                                rint = random.randint(0, 1)
                                path = evening_back_weekend_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodevening_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds[path])
                                turnoff_outlet()

                            else:
                                evening_phrases = ["s_howwasyourafternoon",
                                                   "s_eveningwelcomeback1",
                                                   "s_eveningwelcomeback2"]

                                rint = 0
                                rint = random.randint(0, 1)
                                path = evening_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_welcomeback_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds[path])
                                turnoff_outlet()

                        if seconds_away > 9000:  # longer than 150min
                            if weekday == 4:  # is it friday?

                                evening_phrases = ["s_toosieslide",
                                                   "s_whatspoppin",
                                                   "s_wayout",
                                                   "s_up"]

                                rint = 0
                                rint = random.randint(0, 3)
                                path = evening_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodevening_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_fridayheresmusic_m'])
                                play_sound(sounds[path])
                                turnoff_outlet()

                            if weekday == 5:  # is it saturday?

                                evening_phrases = ["s_toosieslide",
                                                   "s_whatspoppin",
                                                   "s_wayout",
                                                   "s_up"]

                                rint = 0
                                rint = random.randint(0, 3)
                                path = evening_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodevening_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_saturdaysequence_m'])
                                play_sound(sounds[path])
                                turnoff_outlet()

                            if 0 <= weekday <= 3 or weekday == 6:  # between sunday - thursday

                                evening_phrases = ["s_withoutyou",
                                                   "s_allyourn",
                                                   "s_watermelonsugar",
                                                   "s_sevensummers",]

                                rint = 0
                                rint = random.randint(0, 3)
                                path = evening_phrases[rint]

                                time.sleep(1.0)
                                play_sound(sounds['s_wake'])
                                play_sound(sounds['s_goodevening_g'])
                                bright_lights_on()
                                time.sleep(1.0)
                                play_sound(sounds['s_howssomemusic_m'])
                                play_sound(sounds[path])
                                turnoff_outlet()

                    elif latenight_start <= now_time <= latenight_end:  # LATE NIGHT

                        if seconds_away > 3600:  # longer than 60min
                            if 4 <= weekday <= 6:
                                send_text('Front door has been opened.\n\nEnjoy your late night sir.\n\n-M.O.R.G.')

                            if 0 <= weekday <= 3:
                                send_text(
                                    'Front door has been opened.\n\nLate night I see? Get some rest for the morning '
                                    'sir.\n\n-M.O.R.G.')

                            time.sleep(1.0)
                            play_sound(sounds['s_wake'])
                            play_sound(sounds['s_dimlight'])
                            dim_lights_on()
                            time.sleep(1.0)
                            play_sound(sounds['s_lightson'])
                            play_sound(sounds['s_welcomeback_g'])
                            turnoff_outlet()

                    time.sleep(420.0)


    except:
        ex = sys.exc_info()
        send_text('ERROR!\n\n' + str(ex) + '\n\n-M.O.R.G.')
        morg_log.error(str(ex))
        os.remove("/tmp/mydaemon.pid")

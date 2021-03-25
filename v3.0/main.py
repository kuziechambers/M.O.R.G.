import time
import datetime as dt
from datetime import time as ti
import os
import sys
import traceback
import secrets
import simpleaudio as audio
import random
import os
from twilio.rest import Client

from text_service import send_text
from constants_sound import *
from constants_time import *
from state_events import *




# Grab and write pid to .pid file
pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"
logfile = open(pidfile,"w").write(pid)


# Send startup text
#send_text('Script booted sir.\n\n-M.O.R.G.')
 
 
# Initiate last_motion time
last_motion = grab_last_motion_line()


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
        print(str(now_date) +
              " | " +
              str(now_time) +
              " ----- motionstatus: "
              + str(motion) + ",  switchstatus: " + str(switch) + ",  secondsaway: " + str(seconds_away) +
              ",  lastmotion: " + str(last_motion_date) + " | " + str(last_motion_time))
        
        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+") 
        logfile.write(str(now_date) +
              " | " +
              str(now_time) +
              " ----- motionstatus: "
              + str(motion) + ",  switchstatus: " + str(switch) + ",  secondsaway: " + str(seconds_away) +
              ",  lastmotion: " + str(last_motion_date) + " | " + str(last_motion_time))
        logfile.write("\n")
        logfile.close()
        
        a_file = open("/home/pi/M.O.R.G./logs/MORG.log", "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[6] 
        
        new_file = open("/home/pi/M.O.R.G./logs/MORG.log", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()
        
        
        # Inside
        if switch == "inside":
            if motion is False: # Inside - False
                time.sleep(2.0)
            
            if motion is True: # Inside - True
                last_motion = dt.datetime.now()
                time.sleep(30.0)
                
        # Outside
        if switch == "outside":
            if motion is False: # Outside - False
                play_sound(s_ping)

                if 36000 < seconds_away < 36007 and morning_start_away <= now_time <= morning_end_away:
                    send_text('Good morning sir.\nI slept quite well last night without your being here.\n\n-M.O.R.G.')

                if 115200 < seconds_away < 115207 and afternoon_start_away <= now_time <= afternoon_end_away:
                    send_text('Greetings Mr.Chambers,\nI hope you are having a wonderful time away sir.\n\n-M.O.R.G.')
                    
                if 14400 < seconds_away < 14407 and evening_start_away <= now_time <= evening_end_away:
                    send_text('Good evening sir,\nEnjoying your night I hope.\n\n-M.O.R.G.')

  
            if motion is True: # Outside - True
                
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


                if ready is True: # Time to trigger greeting
                    
                    if morning_start <= now_time <= morning_end: # MORNING
                        
                        send_text('Front door has been opened.\n\nGood morning sir.\n\n-M.O.R.G.')
                        
                        time.sleep(1.0)
                        play_sound(s_wake2)
                        play_sound(s_goodmorning)
                        play_sound(s_brightlightseq)
                        bright_lights_on()
                        play_sound(s_sequencecomplete)
                        

                    elif afternoon_start <= now_time <= afternoon_end: # AFTERNOON

                        if 10 < seconds_away < 3600: # between 10s - 60min
                                
                                send_text('Front door has been opened.\n\nWelcome back sir.\n\n-M.O.R.G.')
                                
                                play_sound(s_wake2)
                                play_sound(s_goodafternoon)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                        
                        elif seconds_away > 3600: # longer than 60min
                            afternoon_text_phrases = ["Good afternoon sir.",
                                                      "Hope you're having a wonderful afternoon."]
                            rint = 0
                            rint = random.randint(0,1)
                            text_phrase = afternoon_text_phrases[rint]
                            send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')
                            
                            if weekday == 5 and seconds_away > 6000: # is it saturday?
                            
                                saturdayphrases = [s_saturdaybackinblack,
                                                   s_saturdayhighwaytohell]

                                rint = 0
                                rint = random.randint(0,1)
                                path = saturdayphrases[rint]
                                
                                time.sleep(1.0)
                                play_sound(s_wake2)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                                play_sound(path)

                            else:
                                if seconds_away < 9000: #between 60min - 150min
                            
                                    afternoonphrases = [s_goodafternoon,
                                                        s_welcomemrchambers1,
                                                        s_productiveday2]

                                    rint = 0
                                    rint = random.randint(0,2)
                                    path = afternoonphrases[rint]
                                    
                                    time.sleep(1.0)
                                    play_sound(s_wake2)
                                    play_sound(path)
                                    play_sound(s_brightlightseq)
                                    bright_lights_on()
                                    play_sound(s_sequencecomplete)
                                
                                if seconds_away > 9000: #longer than 150min
                            
                                    afternoonphrases = [s_sevensummers,
                                                        s_withoutyou,
                                                        s_allyourn,
                                                        s_watermelonsugar]
     
                                    rint = 0
                                    rint = random.randint(0,3)
                                    path = afternoonphrases[rint]
                                    
                                    time.sleep(1.0)
                                    play_sound(s_wake2)
                                    play_sound(s_brightlightseq)
                                    bright_lights_on()
                                    play_sound(s_sequencecomplete)
                                    play_sound(path)
 
                    elif evening_start <= now_time <= evening_end: # EVENING
                        
                        evening_text_phrases = ["Good evening sir.",
                                                "Make the most of your evening sir."]
                        rint = 0
                        rint = random.randint(0,1)
                        text_phrase = evening_text_phrases[rint]
                        send_text('Front door has been opened.\n\n' + str(text_phrase) + '\n\n-M.O.R.G.')
                            
                        if seconds_away > 1500 and seconds_away < 3600: # between 25min - 60min
                            if 4 <= weekday <= 6: # between friday - saturday
                                
                                eveningbackweekendphrases = [s_goodevening,
                                                             s_anyplans,
                                                             s_howwasyourafternoon]

                                rint = 0
                                rint = random.randint(0,2)
                                path = eveningbackweekendphrases[rint]
                                
                                time.sleep(1.0)
                                play_sound(s_wake2)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                                play_sound(path)
                            
                            else:
                                
                                time.sleep(1.0)
                                play_sound(s_wake2)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                                play_sound(s_goodevening)
                        
                        if seconds_away > 3600 and seconds_away < 9000: # between 60min - 150min
                        
                            eveningphrases = [s_welcomehomesir,
                                              s_welcomemrchambers1,
                                              s_anyplans,
                                              s_productiveday2]

                            rint = 0
                            rint = random.randint(0,3)
                            path = eveningphrases[rint]
                            
                            time.sleep(1.0)
                            play_sound(s_wake2)
                            play_sound(s_brightlightseq)
                            bright_lights_on()
                            play_sound(s_sequencecomplete)
                            play_sound(path)
                            
                        if seconds_away > 9000: # longer than 150min
                            if 4 <= weekday <= 5: # between friday - saturday
                            
                                eveningphrases = [s_holidaylilnasx,
                                                  s_whatspoppin,
                                                  s_wayout,
                                                  s_up]

                                rint = 0
                                rint = random.randint(0,3)
                                path = eveningphrases[rint]
                                
                                time.sleep(1.0)
                                play_sound(s_wake2)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                                play_sound(path)
                                
                            if 0 <= weekday <= 3 or weekday == 6: # between sunday - thursday
                            
                                eveningphrases = [s_withoutyou,
                                                  s_allyourn,
                                                  s_wayout,
                                                  s_watermelonsugar,
                                                  s_sevensummers,
                                                  s_up]

                                rint = 0
                                rint = random.randint(0,5)
                                path = eveningphrases[rint]
                                
                                time.sleep(1.0)
                                play_sound(s_wake2)
                                play_sound(s_brightlightseq)
                                bright_lights_on()
                                play_sound(s_sequencecomplete)
                                play_sound(path)

                    elif latenight_start <= now_time <= latenight_end: # LATE NIGHT
                            
                        if seconds_away > 3600: # longer than 60min
                            if 4 <= weekday <= 6:
                                send_text('Front door has been opened.\n\nEnjoy your late night sir.\n\n-M.O.R.G.')
                                
                            if 0 <= weekday <= 3:
                                send_text('Front door has been opened.\n\nLate night I see? Get some rest for the morning sir.\n\n-M.O.R.G.')
                            
                            time.sleep(1.0)
                            play_sound(s_wake2)
                            play_sound(s_welcomehomesir)
                            play_sound(s_dimmedlightseq)
                            dim_lights_on()
                            play_sound(s_sequencecomplete)
                                
                                
                    time.sleep(420.0)
                                 
        
    except:
        e = sys.exc_info()
        send_text('ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
        logfile = open("/home/pi/M.O.R.G./logs/MORG.log","a+") 
        logfile.write(str(e))
        logfile.write("\n")
        logfile.close()
        os.remove("/tmp/mydaemon.pid")
        


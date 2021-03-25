import time
import datetime as dt
from datetime import time as ti
import os
import sys
import json
import requests
import logging
from logging.handlers import RotatingFileHandler
import traceback
import secrets
import simpleaudio as audio
import random
import smtplib

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dirName = os.path.dirname(os.path.realpath(__file__))
handler = RotatingFileHandler(os.path.join(dirName, 'pir.log'), maxBytes=20 * 1024 * 1024)
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


logfile = open("/home/pi/Documents/Other files/MORG.log","a+") 
 
#time.sleep(20.0)

s_anycompany = "/home/pi/Documents/MORGsounds/anycompany.wav"
s_anyplans = "/home/pi/Documents/MORGsounds/anyplans.wav"
s_brightlight = "/home/pi/Documents/MORGsounds/brightlight.wav"
s_dimmedlight = "/home/pi/Documents/MORGsounds/dimmedlight.wav"
s_echobackinblack = "/home/pi/Documents/MORGsounds/echobackinblack.wav"
s_echoCFB = "/home/pi/Documents/MORGsounds/echoCFB.wav"
s_echohighwaytohell = "/home/pi/Documents/MORGsounds/echohighwaytohell.wav"
s_goodafternoon = "/home/pi/Documents/MORGsounds/goodafternoon.wav"
s_goodevening = "/home/pi/Documents/MORGsounds/goodevening.wav"
s_goodmorning = "/home/pi/Documents/MORGsounds/goodmorning.wav"
s_heressomemusic = "/home/pi/Documents/MORGsounds/heressomemusic.wav"
s_holidaylilnasx = "/home/pi/Documents/MORGsounds/holidaylilnasx.wav"
s_howssomemusic = "/home/pi/Documents/MORGsounds/howssomemusic.wav"
s_howwasyourafternoon = "/home/pi/Documents/MORGsounds/howwasyourafternoon.wav"
s_productiveday1 = "/home/pi/Documents/MORGsounds/productiveday1.wav"
s_productiveday2 = "/home/pi/Documents/MORGsounds/productiveday2.wav"
s_saturdaybackinblack = "/home/pi/Documents/MORGsounds/saturdaybackinblack.wav"
s_saturdayhighwaytohell = "/home/pi/Documents/MORGsounds/saturdayhighwaytohell.wav"
s_chiquita = "/home/pi/Documents/MORGsounds/chiquita2.wav"
s_whatspoppin = "/home/pi/Documents/MORGsounds/whatspoppin.wav"
s_sequencecomplete = "/home/pi/Documents/MORGsounds/sequencecomplete.wav"
s_welcomemrchambers1 = "/home/pi/Documents/MORGsounds/welcomehomemrchambers1.wav"
s_welcomemrchambers2 = "/home/pi/Documents/MORGsounds/welcomehomemrchambers2.wav"
s_welcomehomesir = "/home/pi/Documents/MORGsounds/welcomehomesir.wav"
s_wake = "/home/pi/Documents/MORGsounds/wake.wav"
s_wake2 = "/home/pi/Documents/MORGsounds/wake3.wav"
s_ping = "/home/pi/Documents/MORGsounds/ping3.wav"
s_quietping = "/home/pi/Documents/MORGsounds/pingquiet.wav"



#time.sleep(25.0)


PIR_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/18'
SWITCH_URL = 'http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/sensors/4'
lastMotion = dt.datetime.now()


def getPirState():
    try:
        response = requests.get(PIR_URL)
        json_data = json.loads(response.text)
        return json_data['state']['presence'] is True
    except:
        logger.exception("exception occurred")
        return False

def getSwitchState():
    try:
        response = requests.get(SWITCH_URL)
        json_data = json.loads(response.text)
        if json_data['state']['buttonevent'] == 1002:
            return "inside"
        if json_data['state']['buttonevent'] == 2002:
            return "inside"
        if json_data['state']['buttonevent'] == 3002:
            return "outside"
        if json_data['state']['buttonevent'] == 4002:
            return "outside"

    except:
        logger.exception("exception occurred")
        return False



logfile.write("\n")
logfile.write("\n")
logfile.write("\n")
logfile.close() 

while True:
    try:
        pir = getPirState()
        switch = getSwitchState()

        now = dt.datetime.now()
        print(now)
        print(pir)
        print(switch)
        print("Last Motion: " + str(lastMotion))
        print()
        
        logfile = open("/home/pi/Documents/Other files/MORG.log","a+") 
        logfile.write(str(now) + "\n")
        logfile.write(str(pir) + "\n")
        logfile.write(str(switch) + "\n")
        logfile.write("Last Motion: " + str(lastMotion) + "\n")
        logfile.write("\n")
        logfile.close()
        
        a_file = open("/home/pi/Documents/Other files/MORG.log", "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[6] 
        del lines[7]
        del lines[8]
        del lines[9]
        del lines[10]
        
        new_file = open("/home/pi/Documents/Other files/MORG.log", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()


        if switch == "inside":
            audio.WaveObject.from_wave_file(s_quietping).play().wait_done()

        if switch == "outside":
            audio.WaveObject.from_wave_file(s_ping).play().wait_done()
            
            morningstart = ti(8, 1, 00, 000000)
            morningend = ti(10, 59, 00, 000000)
            
            afternoonstart = ti(11, 00, 00, 000000)
            afternoonend = ti(19, 00, 00, 000000)
            
            eveningstart = ti(19, 1, 00, 000000)
            eveningend = ti(0, 15, 00, 000000)
            
            nowtime = dt.datetime.now().time()
            
            if 57600 < (now - lastMotion).total_seconds() < 57607 and 3 <= weekday <= 6 and afternoonstart <= nowtime <= afternoonend:
                try:
                    server = smtplib.SMTP( "smtp.gmail.com", 587 )
                    server.starttls()
                    server.login('kuzie.chambers@gmail.com','Kc24962387103!' )
                    server.sendmail('M.O.R.G.','9402311617@mms.att.net','Greetings Mr.Chambers,\nI hope you are having a wonderful time away sir.\n\n-M.O.R.G.')
                    server.quit()
                except:
                    print("Message wasn't sent")
                
            if 36000 < (now - lastMotion).total_seconds() < 36007 and morningstart <= nowtime <= morningend:
                try:
                    server = smtplib.SMTP( "smtp.gmail.com", 587 )
                    server.starttls()
                    server.login('kuzie.chambers@gmail.com','Kc24962387103!' )
                    server.sendmail('M.O.R.G.','9402311617@mms.att.net','Good morning sir.\nI slept quite well last night without your being here.\n\n-M.O.R.G.')
                    server.quit()
                except:
                    print("Message wasn't sent")

            if 25200 < (now - lastMotion).total_seconds() < 25207 and eveningstart <= nowtime <= eveningend:
                try:
                    server = smtplib.SMTP( "smtp.gmail.com", 587 )
                    server.starttls()
                    server.login('kuzie.chambers@gmail.com','Kc24962387103!' )
                    server.sendmail('M.O.R.G.','9402311617@mms.att.net','Good evening sir,\nEnjoying your night I hope.\n\n-M.O.R.G.')
                    server.quit()
                except:
                    print("Message wasn't sent")
        
        
        
        if pir is True:
            if switch == "inside":
                time.sleep(20.0)
            
            if switch == "outside":
                
                linecount = 0
                fname = "/home/pi/Documents/Other files/MORG.log"
                with open(fname, 'r') as f:
                    for line in f:
                        linecount += 1
                
                linetoread1 = linecount - 200
                linetoread2 = linecount - 201
                linetoread3 = linecount - 202
                linetoread4 = linecount - 203
                linetoread5 = linecount - 204
                
                a_file = open("/home/pi/Documents/Other files/MORG.log")
                lines_to_read = [linetoread1,
                                 linetoread2,
                                 linetoread3,
                                 linetoread4,
                                 linetoread5]

                ready = True
                for position, line in enumerate(a_file):
                    if position in lines_to_read:
                        if "inside" in line:
                            print("Found the word inside")
                            ready = False
                            time.sleep(60.0)
                            
                if ready is True:
                    
                    server = smtplib.SMTP( "smtp.gmail.com", 587 )
                    server.starttls()
                    server.login('kuzie.chambers@gmail.com','Kc24962387103!' )
                    server.sendmail('M.O.R.G.','9402311617@mms.att.net','Front door has been opened.\n\n-M.O.R.G.')
                    server.quit()
                    
                    
                    nowtime = dt.datetime.now().time()
                    weekday = dt.datetime.now().weekday()
                    day = dt.datetime.now().day
                    
                    morningstart = ti(8, 00, 00, 000000)
                    morningend = ti(10, 44, 00, 000000)
                    
                    afternoonstart = ti(10, 45, 00, 000000)
                    afternoonend = ti(18, 00, 00, 000000)
                    
                    eveningstart = ti(18, 1, 00, 000000)
                    eveningend = ti(23, 39, 00, 000000)
                    
                    latenightstart = ti(23, 40, 00, 000000)
                    latenightend = ti(1, 55, 00, 000000)
                    
                    if morningstart <= nowtime <= morningend:
                        
                        lastMotion = now
                        
                        time.sleep(1.0)
                        audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                        audio.WaveObject.from_wave_file(s_goodmorning).play().wait_done()
                        
                    elif afternoonstart <= nowtime <= afternoonend:

                        if (now - lastMotion).total_seconds() < 3600 and (now - lastMotion).total_seconds() > 10: # PLAY WELCOME BACK ###CHANGE to 900
                            
                                lastMotion = now
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(s_goodafternoon).play().wait_done()
                        
                        else: #PLAY REGULAR AFTERNOON
                            if weekday == 5:
                                lastMotion = now
                            
                                saturdayphrases = [s_saturdaybackinblack,
                                                   s_saturdayhighwaytohell]

                                rint = random.randint(0,1)
                                path = saturdayphrases[rint]
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(path).play().wait_done()
                            
                            elif (now - lastMotion).total_seconds() > 3600 and (now - lastMotion).total_seconds() < 7200:
                                lastMotion = now
                        
                                afternoonphrases = [s_goodafternoon,
                                                    s_welcomemrchambers1,
                                                    s_productiveday2]

                                rint = random.randint(0,2)
                                path = afternoonphrases[rint]
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(path).play().wait_done()
                                
                            elif (now - lastMotion).total_seconds() > 7200:
                                lastMotion = now
                        
                                afternoonphrases = [s_welcomemrchambers1,
                                                    s_chiquita,
                                                    s_whatspoppin,
                                                    s_holidaylilnasx]
 
                                rint = random.randint(0,3)
                                path = afternoonphrases[rint]
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(path).play().wait_done()

                    elif eveningstart <= nowtime <= eveningend:
                        
                        if (now - lastMotion).total_seconds() < 4800 and (now - lastMotion).total_seconds() > 1500: # PLAY WELCOME BACK
                        
                            if 4 <= weekday <= 6:
                                lastMotion = now
                                
                                eveningbackweekendphrases = [s_goodevening,
                                                             s_anyplans,
                                                             s_howwasyourafternoon]

                                rint = random.randint(0,2)
                                path = eveningbackweekendphrases[rint]
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(path).play().wait_done()
                            
                            else:
                                lastMotion = now
                                
                                time.sleep(1.0)
                                audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                                audio.WaveObject.from_wave_file(s_goodevening).play().wait_done()
                        
                        if (now - lastMotion).total_seconds() < 8400 and (now - lastMotion).total_seconds() > 4800: #PLAY REGULAR EVENING
                            lastMotion = now
                        
                            eveningphrases = [s_welcomehomesir,
                                              s_welcomemrchambers1,
                                              s_anyplans,
                                              s_productiveday2]

                            rint = random.randint(0,3)
                            path = eveningphrases[rint]
                            
                            time.sleep(1.0)
                            audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                            audio.WaveObject.from_wave_file(path).play().wait_done()
                            
                        if (now - lastMotion).total_seconds() > 8400: #PLAY REGULAR EVENING
                            lastMotion = now
                        
                            eveningphrases = [s_welcomehomesir,
                                              s_welcomemrchambers1,
                                              s_anyplans,
                                              s_productiveday2,
                                              s_chiquita,
                                              s_whatspoppin,
                                              s_holidaylilnasx]

                            rint = random.randint(0,6)
                            path = eveningphrases[rint]
                            
                            time.sleep(1.0)
                            audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                            audio.WaveObject.from_wave_file(path).play().wait_done()
                        
                    elif latenightstart <= nowtime <= latenightend:
                        
                        if (now - lastMotion).total_seconds() > 4800: #PLAY REGULAR LATE NIGHT                 
                            lastMotion = now
                            
                            time.sleep(1.0)
                            audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
                            audio.WaveObject.from_wave_file(s_welcomehomesir).play().wait_done()
                                
                                
                    time.sleep(360.0)
                             


        
        time.sleep(0.5)
    except:
        e = sys.exc_info()
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login('kuzie.chambers@gmail.com','Kc24962387103!' )
        server.sendmail('M.O.R.G.','9402311617@mms.att.net','ERROR!\n\n' + str(e) + '\n\n-M.O.R.G.')
        server.quit()
        
logfile.close() 

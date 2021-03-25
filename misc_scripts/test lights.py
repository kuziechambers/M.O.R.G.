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

 
#time.sleep(20.0)

s_anycompany = "/home/pi/Documents/MORGsounds/anycompany.wav"
s_anyplans = "/home/pi/Documents/MORGsounds/anyplans.wav"
s_brightlight = "/home/pi/Documents/MORGsounds/brightlight.wav"
s_brightlightseq = "/home/pi/Documents/MORGsounds/brightlightseq.wav"
s_dimmedlight = "/home/pi/Documents/MORGsounds/dimmedlight.wav"
s_dimmedlightseq = "/home/pi/Documents/MORGsounds/dimmedlightseq.wav"
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

              #### FIX THIS
#audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
#audio.WaveObject.from_wave_file(s_brightlight).play().wait_done()

payload = {
                "on": True,
		"bri": 150,
		"hue": 8402,
		"sat": 140,
          }

audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
audio.WaveObject.from_wave_file(s_goodmorning).play().wait_done()
audio.WaveObject.from_wave_file(s_brightlightseq).play().wait_done()
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps({"on": True,"bri": 254,"hue": 5214,"sat": 88,}))
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(payload))
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(payload))
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(payload))
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(payload))
requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(payload))
audio.WaveObject.from_wave_file(s_sequencecomplete).play().wait_done()

print(r)
print(r.status_code)
print(r.content)




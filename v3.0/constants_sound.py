import json
import requests
import simpleaudio as audio


# sound filenames dictionary
sounds = {
    's_anycompany': "/home/pi/M.O.R.G./sounds_old/anycompany.wav",
    's_anyplans': "/home/pi/M.O.R.G./sounds_old/anyplans.wav",
    's_allyourn': "/home/pi/M.O.R.G./sounds_old/allyourn.wav",
    's_brightlight': "/home/pi/M.O.R.G./sounds_old/brightlight.wav",
    's_brightlightseq': "/home/pi/M.O.R.G./sounds_old/brightlightseq.wav",
    's_chiquita': "/home/pi/M.O.R.G./sounds_old/chiquita2.wav",
    's_dimmedlight': "/home/pi/M.O.R.G./sounds_old/dimmedlight.wav",
    's_dimmedlightseq': "/home/pi/M.O.R.G./sounds_old/dimmedlightseq.wav",
    's_echobackinblack': "/home/pi/M.O.R.G./sounds_old/echobackinblack.wav",
    's_echoCFB': "/home/pi/M.O.R.G./sounds_old/echoCFB.wav",
    's_echohighwaytohell': "/home/pi/M.O.R.G./sounds_old/echohighwaytohell.wav",
    's_freebird': "/home/pi/M.O.R.G./sounds_old/freebird2.wav",
    's_goodafternoon': "/home/pi/M.O.R.G./sounds_old/goodafternoon.wav",
    's_goodevening': "/home/pi/M.O.R.G./sounds_old/goodevening.wav",
    's_goodmorning': "/home/pi/M.O.R.G./sounds_old/goodmorning.wav",
    's_onlygoodmorning': "/home/pi/M.O.R.G./sounds_old/onlygoodmorning.wav",
    's_heressomemusic': "/home/pi/M.O.R.G./sounds_old/heressomemusic.wav",
    's_holidaylilnasx': "/home/pi/M.O.R.G./sounds_old/holidaylilnasx.wav",
    's_howssomemusic': "/home/pi/M.O.R.G./sounds_old/howssomemusic.wav",
    's_howwasyourafternoon': "/home/pi/M.O.R.G./sounds_old/howwasyourafternoon.wav",
    's_productiveday1': "/home/pi/M.O.R.G./sounds_old/productiveday1.wav",
    's_productiveday2': "/home/pi/M.O.R.G./sounds_old/productiveday2.wav",
    's_ping': "/home/pi/M.O.R.G./sounds_old/ping3.wav",
    's_quietping': "/home/pi/M.O.R.G./sounds_old/pingquiet2.wav",
    's_saturdaybackinblack': "/home/pi/M.O.R.G./sounds_old/saturdaybackinblack.wav",
    's_saturdayhighwaytohell': "/home/pi/M.O.R.G./sounds_old/saturdayhighwaytohell.wav",
    's_sequencecomplete': "/home/pi/M.O.R.G./sounds_old/sequencecomplete.wav",
    's_sevensummers': "/home/pi/M.O.R.G./sounds_old/sevensummers.wav",
    's_up': "/home/pi/M.O.R.G./sounds_old/up.wav",
    's_whatspoppin': "/home/pi/M.O.R.G./sounds_old/whatspoppin.wav",
    's_withoutyou': "/home/pi/M.O.R.G./sounds_old/withoutyou.wav",
    's_welcomemrchambers1': "/home/pi/M.O.R.G./sounds_old/welcomehomemrchambers1.wav",
    's_welcomemrchambers2': "/home/pi/M.O.R.G./sounds_old/welcomehomemrchambers2.wav",
    's_welcomehomesir': "/home/pi/M.O.R.G./sounds_old/welcomehomesir.wav",
    's_watermelonsugar': "/home/pi/M.O.R.G./sounds_old/watermelonsugar.wav",
    's_wayout': "/home/pi/M.O.R.G./sounds_old/wayout.wav",
    's_wake': "/home/pi/M.O.R.G./sounds_old/wake.wav",
    's_wake2': "/home/pi/M.O.R.G./sounds_old/wake3.wav"
}

# play sound function
def play_sound(sound_file):
    audio.WaveObject.from_wave_file(sound_file).play().wait_done()


# light payloads
brightpayload = {
        "on": True,
        "bri": 254,
        "hue": 8402,
        "sat": 140,
        }

concentratepayload = {
        "on": True,
        "bri": 254,
        "hue": 39392,
        "sat": 13,
        }

dimpayload = {
        "on": True,
        "bri": 150,
        "hue": 8402,
        "sat": 140,
        }


# turn on lights functions
def bright_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(brightpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(brightpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(brightpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(brightpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(brightpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(brightpayload))

def concentrate_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(concentratepayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(concentratepayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(concentratepayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(concentratepayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(concentratepayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(concentratepayload))

def dim_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(dimpayload))



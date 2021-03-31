import json
import requests
import simpleaudio as audio


# sound filenames dictionary
sounds = {
    's_anycompany': "/home/pi/M.O.R.G./sounds_wav/anycompany.wav",
    's_anyplans': "/home/pi/M.O.R.G./sounds_wav/anyplans.wav",
    's_allyourn': "/home/pi/M.O.R.G./sounds_wav/allyourn.wav",
    's_brightlight': "/home/pi/M.O.R.G./sounds_wav/brightlight.wav",
    's_brightlightseq': "/home/pi/M.O.R.G./sounds_wav/brightlightseq.wav",
    's_chiquita': "/home/pi/M.O.R.G./sounds_wav/chiquita2.wav",
    's_dimmedlight': "/home/pi/M.O.R.G./sounds_wav/dimmedlight.wav",
    's_dimmedlightseq': "/home/pi/M.O.R.G./sounds_wav/dimmedlightseq.wav",
    's_echobackinblack': "/home/pi/M.O.R.G./sounds_wav/echobackinblack.wav",
    's_echoCFB': "/home/pi/M.O.R.G./sounds_wav/echoCFB.wav",
    's_echohighwaytohell': "/home/pi/M.O.R.G./sounds_wav/echohighwaytohell.wav",
    's_freebird': "/home/pi/M.O.R.G./sounds_wav/freebird.wav",
    's_goodafternoon': "/home/pi/M.O.R.G./sounds_wav/goodafternoon.wav",
    's_goodevening': "/home/pi/M.O.R.G./sounds_wav/goodevening.wav",
    's_goodmorning': "/home/pi/M.O.R.G./sounds_wav/goodmorning.wav",
    's_onlygoodmorning': "/home/pi/M.O.R.G./sounds_wav/onlygoodmorning.wav",
    's_heressomemusic': "/home/pi/M.O.R.G./sounds_wav/heressomemusic.wav",
    's_holidaylilnasx': "/home/pi/M.O.R.G./sounds_wav/holidaylilnasx.wav",
    's_howssomemusic': "/home/pi/M.O.R.G./sounds_wav/howssomemusic.wav",
    's_howwasyourafternoon': "/home/pi/M.O.R.G./sounds_wav/howwasyourafternoon.wav",
    's_productiveday1': "/home/pi/M.O.R.G./sounds_wav/productiveday1.wav",
    's_productiveday2': "/home/pi/M.O.R.G./sounds_wav/productiveday2.wav",
    's_ping': "/home/pi/M.O.R.G./sounds_wav/ping3.wav",
    's_quietping': "/home/pi/M.O.R.G./sounds_wav/pingquiet2.wav",
    's_saturdaybackinblack': "/home/pi/M.O.R.G./sounds_wav/saturdaybackinblack.wav",
    's_saturdayhighwaytohell': "/home/pi/M.O.R.G./sounds_wav/saturdayhighwaytohell.wav",
    's_sequencecomplete': "/home/pi/M.O.R.G./sounds_wav/sequencecomplete.wav",
    's_sevensummers': "/home/pi/M.O.R.G./sounds_wav/sevensummers.wav",
    's_up': "/home/pi/M.O.R.G./sounds_wav/up.wav",
    's_whatspoppin': "/home/pi/M.O.R.G./sounds_wav/whatspoppin.wav",
    's_withoutyou': "/home/pi/M.O.R.G./sounds_wav/withoutyou.wav",
    's_welcomemrchambers1': "/home/pi/M.O.R.G./sounds_wav/welcomehomemrchambers1.wav",
    's_welcomemrchambers2': "/home/pi/M.O.R.G./sounds_wav/welcomehomemrchambers2.wav",
    's_welcomehomesir': "/home/pi/M.O.R.G./sounds_wav/welcomehomesir.wav",
    's_watermelonsugar': "/home/pi/M.O.R.G./sounds_wav/watermelonsugar.wav",
    's_wayout': "/home/pi/M.O.R.G./sounds_wav/wayout.wav",
    's_wake': "/home/pi/M.O.R.G./sounds_wav/wake.wav",
    's_wake2': "/home/pi/M.O.R.G./sounds_wav/wake3.wav"
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
    
def dim_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(dimpayload))



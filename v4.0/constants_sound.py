import json
import requests
import simpleaudio as audio


# sound filenames dictionary
sounds = {
    's_anycompany': "/home/pi/M.O.R.G./sounds_IBM/anycompany.wav",
    's_anyplans': "/home/pi/M.O.R.G./sounds_IBM/anyplans.wav",
    's_allyourn': "/home/pi/M.O.R.G./sounds_IBM/AllYourn.wav",
    's_brightlight': "/home/pi/M.O.R.G./sounds_IBM/brightlight.wav",
    's_chiquita': "/home/pi/M.O.R.G./sounds_IBM/Chiquita.wav",
    's_dimlight': "/home/pi/M.O.R.G./sounds_IBM/dimlight.wav",
    's_freebird': "/home/pi/M.O.R.G./sounds_IBM/FreeBird.wav",
    's_fridayheresmusic_m': "/home/pi/M.O.R.G./sounds_IBM/fridayheresmusic.wav",
    's_fridayhowsmusic_m': "/home/pi/M.O.R.G./sounds_IBM/fridayhowsmusic.wav",
    's_fridaymorning': "/home/pi/M.O.R.G./sounds_IBM/fridaymorning.wav",
    's_goodafternoon_g': "/home/pi/M.O.R.G./sounds_IBM/goodafternoon_g.wav",
    's_goodevening_g': "/home/pi/M.O.R.G./sounds_IBM/goodevening_g.wav",
    's_goodmorning_g': "/home/pi/M.O.R.G./sounds_IBM/goodmorning_g.wav",
    's_lightson': "/home/pi/M.O.R.G./sounds_IBM/lightson.wav",
    's_mondaymorning': "/home/pi/M.O.R.G./sounds_IBM/mondaymorning.wav",
    's_morninggreatday': "/home/pi/M.O.R.G./sounds_IBM/morninggreatday.wav",
    's_morningproductive': "/home/pi/M.O.R.G./sounds_IBM/morningproductive.wav",
    's_morninghadfun': "/home/pi/M.O.R.G./sounds_IBM/morninghadfun.wav",
    's_morningproductiveday': "/home/pi/M.O.R.G./sounds_IBM/morningproductiveday.wav",
    's_morningsleptwell': "/home/pi/M.O.R.G./sounds_IBM/morningsleptwell.wav",
    's_heressomemusic_m': "/home/pi/M.O.R.G./sounds_IBM/heressomemusic.wav",
    's_holiday': "/home/pi/M.O.R.G./sounds_IBM/Holiday.wav",
    's_howssomemusic_m': "/home/pi/M.O.R.G./sounds_IBM/howssomemusic.wav",
    's_howwasyourafternoon': "/home/pi/M.O.R.G./sounds_IBM/howwasyourafternoon.wav",
    's_productiveday_m': "/home/pi/M.O.R.G./sounds_IBM/productiveday.wav",
    's_ping': "/home/pi/M.O.R.G./sounds_IBM/ping3.wav",
    's_quietping': "/home/pi/M.O.R.G./sounds_IBM/pingquiet2.wav",
    's_saturdaybackinblack_m': "/home/pi/M.O.R.G./sounds_IBM/saturdaybackinblack.wav",
    's_saturdayhighwaytohell_m': "/home/pi/M.O.R.G./sounds_IBM/saturdayhighwaytohell.wav",
    's_saturdayheresmusic_m': "/home/pi/M.O.R.G./sounds_IBM/saturdayheresmusic.wav",
    's_saturdayhowsmusic_m': "/home/pi/M.O.R.G./sounds_IBM/saturdayhowsmusic.wav",
    's_saturdaysequence_m': "/home/pi/M.O.R.G./sounds_IBM/saturdaysequence.wav",
    's_sevensummers': "/home/pi/M.O.R.G./sounds_IBM/7summers.wav",
    's_tuesdaymorning': "/home/pi/M.O.R.G./sounds_IBM/tuesdaymorning.wav",
    's_thursdaymorning': "/home/pi/M.O.R.G./sounds_IBM/thursdaymorning.wav",
    's_toosieslide': "/home/pi/M.O.R.G./sounds_IBM/ToosieSlide.wav",
    's_up': "/home/pi/M.O.R.G./sounds_IBM/Up.wav",
    's_wednesdaymorning': "/home/pi/M.O.R.G./sounds_IBM/wednesdaymorning.wav",
    's_whatspoppin': "/home/pi/M.O.R.G./sounds_IBM/WhatsPoppin.wav",
    's_withoutyou': "/home/pi/M.O.R.G./sounds_IBM/WithoutYou.wav",
    's_welcomemrchambers_g': "/home/pi/M.O.R.G./sounds_IBM/mrchambers_g.wav",
    's_welcomehome_g': "/home/pi/M.O.R.G./sounds_IBM/welcomehome_g.wav",
    's_welcomeback_g': "/home/pi/M.O.R.G./sounds_IBM/welcomeback_g.wav",
    's_watermelonsugar': "/home/pi/M.O.R.G./sounds_IBM/WatermelonSugar.wav",
    's_wayout': "/home/pi/M.O.R.G./sounds_IBM/Wayout.wav",
    's_wake': "/home/pi/M.O.R.G./sounds_IBM/wake.wav"
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



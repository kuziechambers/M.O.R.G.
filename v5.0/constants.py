import json
import os
import requests
import simpleaudio as audio
from datetime import time as ti


sounds = {
    's_afternoonwelcomeback1': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/afternoonwelcomeback1.wav",
    's_afternoonwelcomeback2': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/afternoonwelcomeback2.wav",
    's_anycompany': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/anycompany.wav",
    's_anyplans': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/anyplans.wav",
    's_allyourn': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/AllYourn.wav",
    's_brightlight': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/brightlight.wav",
    's_chiquita': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/Chiquita.wav",
    's_dimlight': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/dimlight.wav",
    's_enjoyweekendweather': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/enjoyweekendweather.wav",
    's_eveningwelcomeback1': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/eveningwelcomeback1.wav",
    's_eveningwelcomeback2': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/eveningwelcomeback2.wav",
    's_freebird': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/FreeBird.wav",
    's_fridayheresmusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/fridayheresmusic.wav",
    's_fridayhowsmusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/fridayhowsmusic.wav",
    's_fridaymorning': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/fridaymorning.wav",
    's_goodafternoon_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/goodafternoon_g.wav",
    's_goodevening_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/goodevening_g.wav",
    's_goodmorning_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/goodmorning_g.wav",
    's_lightson': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/lightson.wav",
    's_mondaymorning': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/mondaymorning.wav",
    's_morninggreatday': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morninggreatday.wav",
    's_morningwelcomeback1': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morningwelcomeback1.wav",
    's_morningwelcomeback2': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morningwelcomeback2.wav",
    's_morningproductive': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morningproductive.wav",
    's_morninghadfun': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morninghadfun.wav",
    's_morningproductiveday': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morningproductiveday.wav",
    's_morningsleptwell': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/morningsleptwell.wav",
    's_heressomemusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/heressomemusic.wav",
    's_holiday': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/Holiday.wav",
    's_howssomemusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/howssomemusic.wav",
    's_howwasyourafternoon': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/howwasyourafternoon.wav",
    's_productiveday_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/productiveday.wav",
    's_ping': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/ping3.wav",
    's_quietping': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/pingquiet2.wav",
    's_rainchance': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/rainchance.wav",
    's_saturdaylow': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdaylow.wav",
    's_sundaylow': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/sundaylow.wav",
    's_saturdaybackinblack_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdaybackinblack.wav",
    's_saturdayhighwaytohell_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdayhighwaytohell.wav",
    's_saturdayheresmusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdayheresmusic.wav",
    's_saturdayhowsmusic_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdayhowsmusic.wav",
    's_saturdaysequence_m': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/saturdaysequence.wav",
    's_sevensummers': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/7summers.wav",
    's_temprightnow': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/temprightnow.wav",
    's_templow': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/templow.wav",
    's_temphigh': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/temphigh.wav",
    's_tuesdaymorning': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/tuesdaymorning.wav",
    's_thursdaymorning': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/thursdaymorning.wav",
    's_toosieslide': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/ToosieSlide.wav",
    's_up': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/Up.wav",
    's_wednesdaymorning': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/wednesdaymorning.wav",
    's_whatspoppin': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/WhatsPoppin.wav",
    's_withoutyou': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/WithoutYou.wav",
    's_welcomemrchambers_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/mrchambers_g.wav",
    's_welcomehome_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/welcomehome_g.wav",
    's_welcomeback_g': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/welcomeback_g.wav",
    's_watermelonsugar': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/WatermelonSugar.wav",
    's_wayout': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/WayOut.wav",
    's_wake': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/wake.wav"
}

time_sounds = {
    's_zero': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/zero.wav",
    's_one': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/one.wav",
    's_two': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/two.wav",
    's_three': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/three.wav",
    's_four': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/four.wav",
    's_five': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/five.wav",
    's_six': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/six.wav",
    's_seven': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/seven.wav",
    's_eight': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/eight.wav",
    's_nine': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/nine.wav",
    's_ten': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/ten.wav",
    's_oneone': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/oneone.wav",
    's_onetwo': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onetwo.wav",
    's_onethree': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onethree.wav",
    's_onefour': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onefour.wav",
    's_onefive': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onefive.wav",
    's_onesix': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onesix.wav",
    's_oneseven': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/oneseven.wav",
    's_oneeight': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/oneeight.wav",
    's_onenine': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/onenine.wav",
    's_twozero': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/twozero.wav",
    's_twoone': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/twoone.wav",
    's_twotwo': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/twotwo.wav",
    's_twothree': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/times/twothree.wav",
}

degrees_sounds = {
    's_degrees': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/degrees.wav",
    's_40below': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/40below.wav",
    's_40': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/40.wav",
    's_41': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/41.wav",
    's_42': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/42.wav",
    's_43': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/43.wav",
    's_44': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/44.wav",
    's_45': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/45.wav",
    's_46': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/46.wav",
    's_47': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/47.wav",
    's_48': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/48.wav",
    's_49': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/49.wav",
    's_50': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/50.wav",
    's_51': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/51.wav",
    's_52': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/52.wav",
    's_53': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/53.wav",
    's_54': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/54.wav",
    's_55': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/55.wav",
    's_56': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/56.wav",
    's_57': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/57.wav",
    's_58': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/58.wav",
    's_59': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/59.wav",
    's_60': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/60.wav",
    's_61': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/61.wav",
    's_62': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/62.wav",
    's_63': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/63.wav",
    's_64': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/64.wav",
    's_65': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/65.wav",
    's_66': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/66.wav",
    's_67': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/67.wav",
    's_68': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/68.wav",
    's_69': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/69.wav",
    's_70': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/70.wav",
    's_71': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/71.wav",
    's_72': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/72.wav",
    's_73': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/73.wav",
    's_74': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/74.wav",
    's_75': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/75.wav",
    's_76': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/76.wav",
    's_77': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/77.wav",
    's_78': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/78.wav",
    's_79': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/79.wav",
    's_80': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/80.wav",
    's_81': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/81.wav",
    's_82': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/82.wav",
    's_83': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/83.wav",
    's_84': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/84.wav",
    's_85': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/85.wav",
    's_86': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/86.wav",
    's_87': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/87.wav",
    's_88': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/88.wav",
    's_89': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/89.wav",
    's_90': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/90.wav",
    's_91': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/91.wav",
    's_92': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/92.wav",
    's_93': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/93.wav",
    's_94': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/94.wav",
    's_95': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/95.wav",
    's_96': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/96.wav",
    's_97': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/97.wav",
    's_98': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/98.wav",
    's_99': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/99.wav",
    's_100': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/100.wav",
    's_101': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/101.wav",
    's_102': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/102.wav",
    's_103': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/103.wav",
    's_104': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/104.wav",
    's_105': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/105.wav",
    's_105over': "/Users/kuziechambers/PyCharmProjects/M.O.R.G./sounds/degrees/105over.wav",
}

def get_degrees_sound(degrees):
    if degrees < 40:
        return degrees_sounds['s_40below']
    elif degrees > 105:
        return degrees_sounds['s_105over']
    else:
        s_string = "s_" + str(degrees)
        return degrees_sounds[s_string]

# play sound function
def play_sound(sound_file):
    #playsound(sound_file)
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
offpayload = {
        "on": False
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
def morning_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps({"on": True,"bri": 254,"hue": 8645,"sat": 114,}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps({"on": True,"bri": 127,"hue": 8645,"sat": 114,}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps({"on": True,"bri": 178,"hue": 8645,"sat": 114,}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps({"on": True,"bri": 178,"hue": 8645,"sat": 114,}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps({"on": True,"bri": 127,"hue": 8645,"sat": 114,}))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps({"on": True,"bri": 254,"hue": 8645,"sat": 114,}))
def dim_lights_on():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(dimpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(dimpayload))
def all_lights_off():
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/9/state/", data=json.dumps(offpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/5/state/", data=json.dumps(offpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/10/state/", data=json.dumps(offpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/11/state/", data=json.dumps(offpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/12/state/", data=json.dumps(offpayload))
    requests.put("http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/13/state/", data=json.dumps(offpayload))
def turn_on_light(text):
    light_id2=0
    if "bedroom lamp" in text or "bedroom light" in text:
        light_id = 1
    if "mirror light" in text or "mirror lamp" in text:
        light_id = 5
    if "ceiling light" in text:
        light_id = 7
        light_id2 = 8
    if "studio light" in text or "studio lamp" in text or "office light" in text or "office lamp" in text:
        light_id = 9
    if "tv lights" in text:
        light_id = 10
        light_id2 = 11
    if "table lamp" in text or "table light" in text or "living room lamp" in text or "living room light" in text:
        light_id = 12
    if "tower lamp" in text or "tower light" in text:
        light_id = 13

    if light_id2 == 0:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        requests.put(url, data=json.dumps(concentratepayload))
    else:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        url2 = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id2) + "/state/"
        requests.put(url, data=json.dumps(concentratepayload))
        requests.put(url2, data=json.dumps(concentratepayload))
def turn_off_light(text):
    light_id2=0
    if "bedroom lamp" in text or "bedroom light" in text:
        light_id = 1
    if "mirror light" in text or "mirror lamp" in text:
        light_id = 5
    if "ceiling light" in text:
        light_id = 7
        light_id2 = 8
    if "studio light" in text or "studio lamp" in text or "office light" in text or "office lamp" in text:
        light_id = 9
    if "tv lights" in text:
        light_id = 10
        light_id2 = 11
    if "table lamp" in text or "table light" in text or "living room lamp" in text or "living room light" in text:
        light_id = 12
    if "tower lamp" in text or "tower light" in text:
        light_id = 13

    if light_id2 == 0:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        requests.put(url, data=json.dumps(offpayload))
    else:
        url = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id) + "/state/"
        url2 = "http://192.168.50.205/api/NPrGKaa9jAUUxTkgEywjfapFxy3417zfM81TKZd1/lights/" + str(light_id2) + "/state/"
        requests.put(url, data=json.dumps(offpayload))
        requests.put(url2, data=json.dumps(offpayload))


#--------- TIME ---------------

# away times
morning_start_away = ti(7, 00, 00, 000000)
morning_end_away = ti(10, 59, 59, 000000)

afternoon_start_away = ti(11, 00, 00, 000000)
afternoon_end_away = ti(19, 00, 59, 000000)

evening_start_away = ti(19, 1, 00, 000000)
evening_end_away = ti(22, 00, 00, 000000)

# arriving times
morning_start_office = ti(7, 15, 00, 000000)
morning_end_office = ti(9, 45, 00, 000000)

morning_start = ti(8, 00, 00, 000000)
morning_end = ti(10, 59, 59, 000000)

afternoon_start = ti(11, 00, 00, 000000)
afternoon_end = ti(17, 14, 59, 000000)

evening_start = ti(17, 15, 00, 000000)
evening_end = ti(23, 44, 59, 000000)

latenight_start = ti(23, 55, 00, 000000)
latenight_end = ti(1, 55, 00, 000000)

weekend_start = ti(17, 41, 00, 000000)
weekend_end = ti(17, 46, 10, 000000)

def time_to_sound(time):
    if time == "00:00:00":
        return time_sounds['s_zero']
    if time == "01:00:00":
        return time_sounds['s_one']
    if time == "02:00:00":
        return time_sounds['s_two']
    if time == "03:00:00":
        return time_sounds['s_three']
    if time == "04:00:00":
        return time_sounds['s_four']
    if time == "05:00:00":
        return time_sounds['s_five']
    if time == "06:00:00":
        return time_sounds['s_six']
    if time == "07:00:00":
        return time_sounds['s_seven']
    if time == "08:00:00":
        return time_sounds['s_eight']
    if time == "09:00:00":
        return time_sounds['s_nine']
    if time == "10:00:00":
        return time_sounds['s_ten']
    if time == "11:00:00":
        return time_sounds['s_oneone']
    if time == "12:00:00":
        return time_sounds['s_onetwo']
    if time == "13:00:00":
        return time_sounds['s_onethree']
    if time == "14:00:00":
        return time_sounds['s_onefour']
    if time == "15:00:00":
        return time_sounds['s_onefive']
    if time == "16:00:00":
        return time_sounds['s_onesix']
    if time == "17:00:00":
        return time_sounds['s_oneseven']
    if time == "18:00:00":
        return time_sounds['s_oneeight']
    if time == "19:00:00":
        return time_sounds['s_onenine']
    if time == "20:00:00":
        return time_sounds['s_twozero']
    if time == "21:00:00":
        return time_sounds['s_twoone']
    if time == "22:00:00":
        return time_sounds['s_twotwo']
    if time == "23:00:00":
        return time_sounds['s_twothree']


def turnoff_outlet():
    os.system('sthelper turnoff "M.O.R.G. Light"')

def turnon_outlet():
    os.system('sthelper turnon "M.O.R.G. Light"')

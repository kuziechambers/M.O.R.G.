import json
import os
import requests
import simpleaudio as audio
from datetime import time as ti


sounds = {
    's_afternoonwelcomeback1': "/home/pi/M.O.R.G./sounds/afternoonwelcomeback1.wav",
    's_afternoonwelcomeback2': "/home/pi/M.O.R.G./sounds/afternoonwelcomeback2.wav",
    's_anycompany': "/home/pi/M.O.R.G./sounds/anycompany.wav",
    's_anyplans': "/home/pi/M.O.R.G./sounds/anyplans.wav",
    's_allyourn': "/home/pi/M.O.R.G./sounds/AllYourn.wav",
    's_brightlight': "/home/pi/M.O.R.G./sounds/brightlight.wav",
    's_chiquita': "/home/pi/M.O.R.G./sounds/Chiquita.wav",
    's_dimlight': "/home/pi/M.O.R.G./sounds/dimlight.wav",
    's_enjoyweekendweather': "/home/pi/M.O.R.G./sounds/enjoyweekendweather.wav",
    's_eveningwelcomeback1': "/home/pi/M.O.R.G./sounds/eveningwelcomeback1.wav",
    's_eveningwelcomeback2': "/home/pi/M.O.R.G./sounds/eveningwelcomeback2.wav",
    's_freebird': "/home/pi/M.O.R.G./sounds/FreeBird.wav",
    's_fridayheresmusic_m': "/home/pi/M.O.R.G./sounds/fridayheresmusic.wav",
    's_fridayhowsmusic_m': "/home/pi/M.O.R.G./sounds/fridayhowsmusic.wav",
    's_fridaymorning': "/home/pi/M.O.R.G./sounds/fridaymorning.wav",
    's_goodafternoon_g': "/home/pi/M.O.R.G./sounds/goodafternoon_g.wav",
    's_goodevening_g': "/home/pi/M.O.R.G./sounds/goodevening_g.wav",
    's_goodmorning_g': "/home/pi/M.O.R.G./sounds/goodmorning_g.wav",
    's_lightson': "/home/pi/M.O.R.G./sounds/lightson.wav",
    's_mondaymorning': "/home/pi/M.O.R.G./sounds/mondaymorning.wav",
    's_morninggreatday': "/home/pi/M.O.R.G./sounds/morninggreatday.wav",
    's_morningwelcomeback1': "/home/pi/M.O.R.G./sounds/morningwelcomeback1.wav",
    's_morningwelcomeback2': "/home/pi/M.O.R.G./sounds/morningwelcomeback2.wav",
    's_morningproductive': "/home/pi/M.O.R.G./sounds/morningproductive.wav",
    's_morninghadfun': "/home/pi/M.O.R.G./sounds/morninghadfun.wav",
    's_morningproductiveday': "/home/pi/M.O.R.G./sounds/morningproductiveday.wav",
    's_morningsleptwell': "/home/pi/M.O.R.G./sounds/morningsleptwell.wav",
    's_heressomemusic_m': "/home/pi/M.O.R.G./sounds/heressomemusic.wav",
    's_holiday': "/home/pi/M.O.R.G./sounds/Holiday.wav",
    's_howssomemusic_m': "/home/pi/M.O.R.G./sounds/howssomemusic.wav",
    's_howwasyourafternoon': "/home/pi/M.O.R.G./sounds/howwasyourafternoon.wav",
    's_productiveday_m': "/home/pi/M.O.R.G./sounds/productiveday.wav",
    's_ping': "/home/pi/M.O.R.G./sounds/ping3.wav",
    's_quietping': "/home/pi/M.O.R.G./sounds/pingquiet2.wav",
    's_rainchance': "/home/pi/M.O.R.G./sounds/rainchance.wav",
    's_saturdaylow': "/home/pi/M.O.R.G./sounds/saturdaylow.wav",
    's_sundaylow': "/home/pi/M.O.R.G./sounds/sundaylow.wav",
    's_saturdaybackinblack_m': "/home/pi/M.O.R.G./sounds/saturdaybackinblack.wav",
    's_saturdayhighwaytohell_m': "/home/pi/M.O.R.G./sounds/saturdayhighwaytohell.wav",
    's_saturdayheresmusic_m': "/home/pi/M.O.R.G./sounds/saturdayheresmusic.wav",
    's_saturdayhowsmusic_m': "/home/pi/M.O.R.G./sounds/saturdayhowsmusic.wav",
    's_saturdaysequence_m': "/home/pi/M.O.R.G./sounds/saturdaysequence.wav",
    's_sevensummers': "/home/pi/M.O.R.G./sounds/7summers.wav",
    's_temprightnow': "/home/pi/M.O.R.G./sounds/temprightnow.wav",
    's_templow': "/home/pi/M.O.R.G./sounds/templow.wav",
    's_temphigh': "/home/pi/M.O.R.G./sounds/temphigh.wav",
    's_tuesdaymorning': "/home/pi/M.O.R.G./sounds/tuesdaymorning.wav",
    's_thursdaymorning': "/home/pi/M.O.R.G./sounds/thursdaymorning.wav",
    's_toosieslide': "/home/pi/M.O.R.G./sounds/ToosieSlide.wav",
    's_up': "/home/pi/M.O.R.G./sounds/Up.wav",
    's_wednesdaymorning': "/home/pi/M.O.R.G./sounds/wednesdaymorning.wav",
    's_whatspoppin': "/home/pi/M.O.R.G./sounds/WhatsPoppin.wav",
    's_withoutyou': "/home/pi/M.O.R.G./sounds/WithoutYou.wav",
    's_welcomemrchambers_g': "/home/pi/M.O.R.G./sounds/mrchambers_g.wav",
    's_welcomehome_g': "/home/pi/M.O.R.G./sounds/welcomehome_g.wav",
    's_welcomeback_g': "/home/pi/M.O.R.G./sounds/welcomeback_g.wav",
    's_watermelonsugar': "/home/pi/M.O.R.G./sounds/WatermelonSugar.wav",
    's_wayout': "/home/pi/M.O.R.G./sounds/WayOut.wav",
    's_wake': "/home/pi/M.O.R.G./sounds/wake.wav"
}

time_sounds = {
    's_zero': "/home/pi/M.O.R.G./sounds/times/zero.wav",
    's_one': "/home/pi/M.O.R.G./sounds/times/one.wav",
    's_two': "/home/pi/M.O.R.G./sounds/times/two.wav",
    's_three': "/home/pi/M.O.R.G./sounds/times/three.wav",
    's_four': "/home/pi/M.O.R.G./sounds/times/four.wav",
    's_five': "/home/pi/M.O.R.G./sounds/times/five.wav",
    's_six': "/home/pi/M.O.R.G./sounds/times/six.wav",
    's_seven': "/home/pi/M.O.R.G./sounds/times/seven.wav",
    's_eight': "/home/pi/M.O.R.G./sounds/times/eight.wav",
    's_nine': "/home/pi/M.O.R.G./sounds/times/nine.wav",
    's_ten': "/home/pi/M.O.R.G./sounds/times/ten.wav",
    's_oneone': "/home/pi/M.O.R.G./sounds/times/oneone.wav",
    's_onetwo': "/home/pi/M.O.R.G./sounds/times/onetwo.wav",
    's_onethree': "/home/pi/M.O.R.G./sounds/times/onethree.wav",
    's_onefour': "/home/pi/M.O.R.G./sounds/times/onefour.wav",
    's_onefive': "/home/pi/M.O.R.G./sounds/times/onefive.wav",
    's_onesix': "/home/pi/M.O.R.G./sounds/times/onesix.wav",
    's_oneseven': "/home/pi/M.O.R.G./sounds/times/oneseven.wav",
    's_oneeight': "/home/pi/M.O.R.G./sounds/times/oneeight.wav",
    's_onenine': "/home/pi/M.O.R.G./sounds/times/onenine.wav",
    's_twozero': "/home/pi/M.O.R.G./sounds/times/twozero.wav",
    's_twoone': "/home/pi/M.O.R.G./sounds/times/twoone.wav",
    's_twotwo': "/home/pi/M.O.R.G./sounds/times/twotwo.wav",
    's_twothree': "/home/pi/M.O.R.G./sounds/times/twothree.wav",
}

degrees_sounds = {
    's_degrees': "/home/pi/M.O.R.G./sounds/degrees/degrees.wav",
    's_40below': "/home/pi/M.O.R.G./sounds/degrees/40below.wav",
    's_40': "/home/pi/M.O.R.G./sounds/degrees/40.wav",
    's_41': "/home/pi/M.O.R.G./sounds/degrees/41.wav",
    's_42': "/home/pi/M.O.R.G./sounds/degrees/42.wav",
    's_43': "/home/pi/M.O.R.G./sounds/degrees/43.wav",
    's_44': "/home/pi/M.O.R.G./sounds/degrees/44.wav",
    's_45': "/home/pi/M.O.R.G./sounds/degrees/45.wav",
    's_46': "/home/pi/M.O.R.G./sounds/degrees/46.wav",
    's_47': "/home/pi/M.O.R.G./sounds/degrees/47.wav",
    's_48': "/home/pi/M.O.R.G./sounds/degrees/48.wav",
    's_49': "/home/pi/M.O.R.G./sounds/degrees/49.wav",
    's_50': "/home/pi/M.O.R.G./sounds/degrees/50.wav",
    's_51': "/home/pi/M.O.R.G./sounds/degrees/51.wav",
    's_52': "/home/pi/M.O.R.G./sounds/degrees/52.wav",
    's_53': "/home/pi/M.O.R.G./sounds/degrees/53.wav",
    's_54': "/home/pi/M.O.R.G./sounds/degrees/54.wav",
    's_55': "/home/pi/M.O.R.G./sounds/degrees/55.wav",
    's_56': "/home/pi/M.O.R.G./sounds/degrees/56.wav",
    's_57': "/home/pi/M.O.R.G./sounds/degrees/57.wav",
    's_58': "/home/pi/M.O.R.G./sounds/degrees/58.wav",
    's_59': "/home/pi/M.O.R.G./sounds/degrees/59.wav",
    's_60': "/home/pi/M.O.R.G./sounds/degrees/60.wav",
    's_61': "/home/pi/M.O.R.G./sounds/degrees/61.wav",
    's_62': "/home/pi/M.O.R.G./sounds/degrees/62.wav",
    's_63': "/home/pi/M.O.R.G./sounds/degrees/63.wav",
    's_64': "/home/pi/M.O.R.G./sounds/degrees/64.wav",
    's_65': "/home/pi/M.O.R.G./sounds/degrees/65.wav",
    's_66': "/home/pi/M.O.R.G./sounds/degrees/66.wav",
    's_67': "/home/pi/M.O.R.G./sounds/degrees/67.wav",
    's_68': "/home/pi/M.O.R.G./sounds/degrees/68.wav",
    's_69': "/home/pi/M.O.R.G./sounds/degrees/69.wav",
    's_70': "/home/pi/M.O.R.G./sounds/degrees/70.wav",
    's_71': "/home/pi/M.O.R.G./sounds/degrees/71.wav",
    's_72': "/home/pi/M.O.R.G./sounds/degrees/72.wav",
    's_73': "/home/pi/M.O.R.G./sounds/degrees/73.wav",
    's_74': "/home/pi/M.O.R.G./sounds/degrees/74.wav",
    's_75': "/home/pi/M.O.R.G./sounds/degrees/75.wav",
    's_76': "/home/pi/M.O.R.G./sounds/degrees/76.wav",
    's_77': "/home/pi/M.O.R.G./sounds/degrees/77.wav",
    's_78': "/home/pi/M.O.R.G./sounds/degrees/78.wav",
    's_79': "/home/pi/M.O.R.G./sounds/degrees/79.wav",
    's_80': "/home/pi/M.O.R.G./sounds/degrees/80.wav",
    's_81': "/home/pi/M.O.R.G./sounds/degrees/81.wav",
    's_82': "/home/pi/M.O.R.G./sounds/degrees/82.wav",
    's_83': "/home/pi/M.O.R.G./sounds/degrees/83.wav",
    's_84': "/home/pi/M.O.R.G./sounds/degrees/84.wav",
    's_85': "/home/pi/M.O.R.G./sounds/degrees/85.wav",
    's_86': "/home/pi/M.O.R.G./sounds/degrees/86.wav",
    's_87': "/home/pi/M.O.R.G./sounds/degrees/87.wav",
    's_88': "/home/pi/M.O.R.G./sounds/degrees/88.wav",
    's_89': "/home/pi/M.O.R.G./sounds/degrees/89.wav",
    's_90': "/home/pi/M.O.R.G./sounds/degrees/90.wav",
    's_91': "/home/pi/M.O.R.G./sounds/degrees/91.wav",
    's_92': "/home/pi/M.O.R.G./sounds/degrees/92.wav",
    's_93': "/home/pi/M.O.R.G./sounds/degrees/93.wav",
    's_94': "/home/pi/M.O.R.G./sounds/degrees/94.wav",
    's_95': "/home/pi/M.O.R.G./sounds/degrees/95.wav",
    's_96': "/home/pi/M.O.R.G./sounds/degrees/96.wav",
    's_97': "/home/pi/M.O.R.G./sounds/degrees/97.wav",
    's_98': "/home/pi/M.O.R.G./sounds/degrees/98.wav",
    's_99': "/home/pi/M.O.R.G./sounds/degrees/99.wav",
    's_100': "/home/pi/M.O.R.G./sounds/degrees/100.wav",
    's_101': "/home/pi/M.O.R.G./sounds/degrees/101.wav",
    's_102': "/home/pi/M.O.R.G./sounds/degrees/102.wav",
    's_103': "/home/pi/M.O.R.G./sounds/degrees/103.wav",
    's_104': "/home/pi/M.O.R.G./sounds/degrees/104.wav",
    's_105': "/home/pi/M.O.R.G./sounds/degrees/105.wav",
    's_105over': "/home/pi/M.O.R.G./sounds/degrees/105over.wav",
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

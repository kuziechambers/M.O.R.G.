from datetime import time as time

# morg sounds
SOUNDS = {
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
    's_weatherreport1': "/home/pi/M.O.R.G./sounds/weatherreport1.wav",
    's_weatherreport2': "/home/pi/M.O.R.G./sounds/weatherreport2.wav",
    's_weatherreport3': "/home/pi/M.O.R.G./sounds/weatherreport3.wav",
    's_welcomemrchambers_g': "/home/pi/M.O.R.G./sounds/mrchambers_g.wav",
    's_welcomehome_g': "/home/pi/M.O.R.G./sounds/welcomehome_g.wav",
    's_welcomeback_g': "/home/pi/M.O.R.G./sounds/welcomeback_g.wav",
    's_watermelonsugar': "/home/pi/M.O.R.G./sounds/WatermelonSugar.wav",
    's_wayout': "/home/pi/M.O.R.G./sounds/WayOut.wav",
    's_wake': "/home/pi/M.O.R.G./sounds/wake.wav"
}


# time sounds
TIME_SOUNDS = {
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


# light payloads
LIGHT_PAYLOADS = {
    'bright_payload': {"on": True,"bri": 254,"hue": 8402,"sat": 140,},
    'concentrate_payload': {"on": True,"bri": 254,"hue": 39392,"sat": 13,},
    'dim_payload': {"on": True,"bri": 150,"hue": 8402,"sat": 140,},
    'off_payload': {"on": False}
}

# time frames
# away times
TIME_FRAMES = {
    # morning
    'morning_start_away': time(7, 00, 00, 000000),
    'morning_end_away': time(10, 59, 59, 000000),
    'morning_start_office': time(7, 15, 00, 000000),
    'morning_end_office': time(9, 45, 00, 000000),
    'morning_start': time(8, 00, 00, 000000),
    'morning_end': time(10, 59, 59, 000000),
    # afternoon
    'afternoon_start_away': time(11, 00, 00, 000000),
    'afternoon_end_away': time(19, 00, 59, 000000),
    'afternoon_start': time(11, 00, 00, 000000),
    'afternoon_end': time(17, 14, 59, 000000),
    # evening
    'evening_start_away': time(19, 1, 00, 000000),
    'evening_end_away': time(22, 00, 00, 000000),
    'evening_start': time(17, 15, 00, 000000),
    'evening_end': time(23, 44, 59, 000000),
    # latenight
    'latenight_start': time(23, 55, 00, 000000),
    'latenight_end': time(1, 55, 00, 000000),
    # weekend
    'weekend_start': time(17, 5, 00, 000000),
    'weekend_end': time(17, 5, 8, 000000),
    # mavs alert
    'mavs_game_start': time(17, 7, 00, 000000),
    'mavs_game_end': time(17, 7, 8, 000000)
}

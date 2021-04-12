from datetime import time as ti
from constants_sound import time_sounds

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


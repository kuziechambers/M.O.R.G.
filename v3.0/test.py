from text_service import send_text
from state_events import *
from constants_time import *
from constants_sound import *
import random

afternoonphrases = [s_chiquita,
                    s_sevensummers,
                    s_withoutyou,
                    s_allyourn,
                    s_watermelonsugar]

rint = 0
rint = random.randint(0,4)
path = afternoonphrases[rint]
print(path)

# #body = 4 + 3
# #print("shit" + str(body))
# #send_text(body)
# 
# print("sdagfadgadf" +
#       " 123" +
#       " poop")
# 
# import time
# import datetime as dt
# from datetime import time as ti
# 
# weekday = dt.datetime.now().weekday()
# day = dt.datetime.now().day
# print(str(weekday))
# print(str(day))
# 
# last_motion = dt.datetime.now()
# 
# time.sleep(6.5)
# 
# now = dt.datetime.now()
# seconds_away = (now - last_motion).total_seconds()
# print(last_motion)
# print(now)
# print(str(now.day()))
# print(now.time())
# print(seconds_away)
# 
# morningstart = ti(7, 30, 00, 000000)
# morningend = ti(10, 59, 59, 000000)
# 
# afternoonstart = ti(11, 00, 00, 000000)
# afternoonend = ti(19, 00, 59, 000000)
# 
# eveningstart = ti(19, 1, 00, 000000)
# eveningend = ti(22, 00, 00, 000000)
# 
# nowtime = dt.datetime.now().time()
# weekday = dt.datetime.now().weekday()
# #----------------------------------------------------------------------------------------------------------------
# if 5 < seconds_away < 10 and 2 <= weekday <= 3 and afternoonstart <= nowtime <= afternoonend:
#     bright_lights_on()
#     #send_text('Greetings Mr.Chambers,\nI hope you are having a wonderful time away sir.\n\n-M.O.R.G.')
# 
# if 10 < seconds_away < 15 and 2 <= weekday <= 3 and afternoonstart <= nowtime <= afternoonend:
#     send_text('Greetings Mr.Chambers,\nfuckyou.\n\n-M.O.R.G.')



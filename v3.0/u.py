from text_service import send_text
from state_events import since_office_motion_init
from state_events import since_office_motion_update
from constants_time import *
from constants_sound import *
import time

since_office_motion_init()

while True:
    since_office_motion_update()





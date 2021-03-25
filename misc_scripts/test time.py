import datetime as dt
from datetime import time


songstart = time(1, 45, 00, 000000)
songend = time(1, 52, 00, 000000)

nowtime = dt.datetime.now().time()
if songstart <= nowtime <= songend:
    print("yuuup")
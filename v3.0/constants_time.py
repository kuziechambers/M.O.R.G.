import json
import requests
import sys
import time
import datetime as dt
from datetime import time as ti

# away times
morning_start_away = ti(7, 30, 00, 000000)
morning_end_away = ti(10, 59, 59, 000000)

afternoon_start_away = ti(11, 00, 00, 000000)
afternoon_end_away = ti(19, 00, 59, 000000)

evening_start_away = ti(19, 1, 00, 000000)
evening_end_away = ti(22, 00, 00, 000000)


# arriving times
morning_start = ti(8, 00, 00, 000000)
morning_end = ti(10, 59, 59, 000000)

afternoon_start = ti(11, 00, 00, 000000)
afternoon_end = ti(17, 14, 59, 000000)

evening_start = ti(17, 15, 00, 000000)
evening_end = ti(23, 44, 59, 000000)

latenight_start = ti(23, 55, 00, 000000)
latenight_end = ti(1, 55, 00, 000000)


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


#turn on lights functions
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

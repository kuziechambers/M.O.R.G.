import time
import datetime as dt
from datetime import time as ti
import os
import sys
import json
import requests
import logging
from logging.handlers import RotatingFileHandler
import traceback
import secrets
import simpleaudio as audio
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dirName = os.path.dirname(os.path.realpath(__file__))
handler = RotatingFileHandler(os.path.join(dirName, 'pir.log'), maxBytes=20 * 1024 * 1024)
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
import requests
from xml.etree import ElementTree


url = 'http://192.168.50.193:49153/urn/control'

response = requests.get(url)
print(response)
tree = ElementTree.fromstring(response.content)
print(tree)
response = requests.get(url).json
print(response)



# def getSwitchState():
#     try:
#         response = requests.get(SWITCH_URL)
#         json_data = json.loads(response.text)
#         if json_data['state']['buttonevent'] == 3002:
#             return "outside"
#         if json_data['state']['buttonevent'] == 2002:
#             return "inside"
#     except:
#         logger.exception("exception occurred")
#         return False













#/usr/bin/python3
from subprocess import Popen
import sys
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
import simpleaudio as audio
import random
import smtplib


#filename = sys.argv[1]
filename = "/home/pi/Documents/MORGscripts/MORG_v1.5.py"
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True, env = {'PYTHONPATH': os.pathsep.join(sys.path)})
    p.wait()
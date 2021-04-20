import datetime as dt
import time
import random
import os
from flask import Flask, request, jsonify
from playsound import playsound
from twilio.twiml.messaging_response import MessagingResponse
from constants import (bright_lights_on,
                       all_lights_off,
                       turn_on_light,
                       turn_off_light,
                       wiki_search,
                       morning_start, morning_end,
                       afternoon_start, afternoon_end,
                       evening_start, evening_end,
                       latenight_start, latenight_end)
from events_ibm import transcribe_response, prosody_on_text, play_response
from events_sound import record_to_file, record_to_file_wosir
#import wikipedia
from threading import Thread
#from multiprocessing import Queue

# ngrok API Key: 1rLgHkyR7ArlkSmyaxb7m1JDjOv_5pxZJWBfSPULe7EgbpRcV
os.system("cd /home/pi; ./ngrok http -region=us -hostname=morg.ngrok.io -log=stdout 5000 > /dev/null &")

# noinspection PyTypeChecker
class Compute(Thread):
    def __init__(self, request, target):
        Thread.__init__(self)
        self.request = request
        self.target = target

    def run(self):
        if self.target == "sms_listen":
            print("/sms/COMMANDBEGUN: " + self.target)
            print(self.request)
            print(self.request.values.get('Body', None))
            print("Starting recording")
            record_to_file('/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/spoken_input.wav')
            resp = "Done listening."
            print("done")
            return str(resp)

        if self.target == "repeat_that":
            print("/sms/COMMANDBEGUN: " + self.target)
            time.sleep(15)
            print(self.request)
            print(self.request.values.get('Body', None))
            print("Starting recording")
            record_to_file('/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/spoken_input.wav')
            resp = "Done listening."
            print("done")
            return str(resp)

        if self.target == "anything_else":
            print("/sms/COMMANDBEGUN: " + self.target)
            print(self.request)
            print(self.request.values.get('Body', None))
            time.sleep(10)
            anythingelse_phrases = ["/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/anythingelse.wav",
                                    "/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/isthatall.wav",
                                    "/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/willthatbeall.wav"]

            rint = 0
            rint = random.randint(0, 2)
            path = anythingelse_phrases[rint]
            playsound(path)
            print("Starting recording")
            record_to_file_wosir('/Users/kuziechambers/PycharmProjects/M.O.R.G./stt_files/spoken_input.wav')
            resp = "Done listening."
            print("done")
            return str(resp)

        if self.target == "all_bright_lights_on":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            bright_lights_on()
            return

        if self.target == "all_lights_off":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            all_lights_off()
            return

        if self.target == "light_on":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            message = self.request.get_json()
            light = str(message['light'])
            print(light)
            turn_on_light(light)
            return

        if self.target == "light_off":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            message = self.request.get_json()
            light = str(message['light'])
            print(light)
            turn_off_light(light)
            return

        if self.target == "wiki_search":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            message = self.request.get_json()
            wiki_text = str(message['wikitext'])
            wiki_search(wiki_text)
            return

        if self.target == "say_hello":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            message = self.request.get_json()
            print("Hello " + str(message['person']))
            return

        if self.target == "say_hello_two_people":
            print("/convoresponse/COMMANDBEGUN: " + self.target)
            message = self.request.get_json()
            print("Hello " + str(message['person1']) + " and " + str(message['person2']))
            return











app = Flask(__name__)


# noinspection PyTypeChecker
@app.route("/sms", methods=['GET', 'POST'])
def sms_get():
    """Respond to incoming calls with a simple text message."""
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'listen':
        thread_a = Compute(request.__copy__(), "sms_listen")
        thread_a.start()
        return "Processing in background", 200
    else:
        resp.message("Command not recognized.")
        return str(resp), 200



# noinspection PyTypeChecker
@app.route("/convoresponse", methods=['GET', 'POST'])
def convo_response_get():
    """Respond to incoming calls with a simple text message."""
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    message = request.get_json()
    action = message['action']

    print(action)
    if action == "all-lights-on":
        thread_a = Compute(request.__copy__(), "all_bright_lights_on")
        thread_a.start()
        return jsonify({'action': 'all lights on', 'result': 'processing'})
    if action == "all-lights-off":
        thread_a = Compute(request.__copy__(), "all_lights_off")
        thread_a.start()
        return jsonify({'action': 'all lights off', 'result': 'processing'})
    if action == "turn-on-light":
        thread_a = Compute(request.__copy__(), "light_on")
        thread_a.start()
        return jsonify({'action': 'turn light on', 'result': 'processing'})
    if action == "turn-off-light":
        thread_a = Compute(request.__copy__(), "turn-off-light")
        thread_a.start()
        return jsonify({'action': 'turn light off', 'result': 'processing'})
    if action == "wiki-response":
        thread_a = Compute(request.__copy__(), "wiki_search")
        thread_a.start()
        return jsonify({'action': 'wiki', 'result': 'processing'})
    if action == "say-hello":
        thread_a = Compute(request.__copy__(), "say_hello")
        thread_a.start()
        now = dt.datetime.now()
        now_time = now.time()
        if morning_start <= now_time <= morning_end:
            time_greeting = "Good morning"
        elif afternoon_start <= now_time <= afternoon_end:
            time_greeting = "Good afternoon"
        elif evening_start <= now_time <= evening_end or latenight_start <= now_time <= latenight_end:
            time_greeting = "Good evening"
        else:
            time_greeting = "Good day"
        return jsonify({'action': 'hello person', 'result': 'processing', 'time': time_greeting})
    if action == "say-hello-two-people":
        thread_a = Compute(request.__copy__(), "say_hello_two_people")
        thread_a.start()
        now = dt.datetime.now()
        now_time = now.time()
        if str(message['person1']) == str(message['person2']):
            return jsonify({'action': 'hello person', 'result': 'failed'})
        else:
            if morning_start <= now_time <= morning_end:
                time_greeting = "Good morning"
            elif afternoon_start <= now_time <= afternoon_end:
                time_greeting = "Good afternoon"
            elif evening_start <= now_time <= evening_end or latenight_start <= now_time <= latenight_end:
                time_greeting = "Good evening"
            else:
                time_greeting = "Good day"
            return jsonify({'action': 'hello person', 'result': 'processing', 'time': time_greeting, 'samevalues': 'no'})
    if action == "repeat-that":
        thread_b = Compute(request.__copy__(), "repeat_that")
        thread_b.start()
        return jsonify({'action': 'action not found', 'result': 'repeating'})
    if action == "anything-else":
        thread_c = Compute(request.__copy__(), "anything_else")
        thread_c.start()
        return jsonify({'action': 'anything else', 'result': 'repeating'})
    if action == "end-convo":
        return jsonify({'action': 'end convo', 'result': 'ended'})
    else:
        return jsonify({'action': 'action not found', 'result': 'not processing'})



app.run()

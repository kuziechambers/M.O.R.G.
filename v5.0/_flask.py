import datetime as dt
import os
import time
import random
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from constants import (bright_lights_on,
                       all_lights_off,
                       turn_on_light,
                       turn_off_light,
                       play_sound,
                       morning_start, morning_end,
                       afternoon_start, afternoon_end,
                       evening_start, evening_end,
                       latenight_start, latenight_end
                       )
from logger import flask_log
from events_ibm import watson_init_session, watson_delete_session, stt_watson_tts, wiki_search
from events_sports import ask_mavs_game
from threading import Thread

pid = str(os.getpid())
pidfile = "/tmp/flask.pid"
logfile = open(pidfile, "w").write(pid)

# ngrok API Key: 1rLgHkyR7ArlkSmyaxb7m1JDjOv_5pxZJWBfSPULe7EgbpRcV
os.system("cd /home/pi; ./ngrok http -region=us -hostname=morg.ngrok.io -log=stdout 5000 > /home/pi/ngrok.log &")

global convo_id

try:

    # noinspection PyTypeChecker
    class Compute(Thread):
        def __init__(self, req, target):
            Thread.__init__(self)
            self.request = req
            self.target = target

        # noinspection PyUnboundLocalVariable
        def run(self):
            if self.target == "sms_listen":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/sms/COMMANDBEGUN: " + self.target)
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request))
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request.values.get('Body', None)))
                global convo_id
                convo_id = watson_init_session()
                stt_watson_tts(convo_id)
                resp = "Done listening."
                return str(resp)

            if self.target == "repeat_that":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/sms/COMMANDBEGUN: " + self.target)
                time.sleep(5)
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request))
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request.values.get('Body', None)))
                stt_watson_tts(convo_id)
                resp = "Done listening."
                return str(resp)

            if self.target == "anything_else":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/sms/COMMANDBEGUN: " + self.target)
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request))
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + str(self.request.values.get('Body', None)))
                time.sleep(5)
                anythingelse_phrases = ["/home/pi/M.O.R.G./stt_files/anythingelse.wav",
                                        "/home/pi/M.O.R.G./stt_files/isthatall.wav",
                                        "/home/pi/M.O.R.G./stt_files/willthatbeall.wav"]
                rint = random.randint(0, 2)
                path = anythingelse_phrases[rint]
                play_sound(path)
                stt_watson_tts(convo_id)
                resp = "Done listening."
                return str(resp)

            if self.target == "any_greeting":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                return

            if self.target == "all_lights_on":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                bright_lights_on()
                return

            if self.target == "all_lights_off":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                all_lights_off()
                return

            if self.target == "light_on":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                light = str(message['light'])
                flask_log.info(str(now_date) + " | " + str(now_time) + light)
                turn_on_light(light)
                return

            if self.target == "light_off":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                light = str(message['light'])
                flask_log.info(str(now_date) + " | " + str(now_time) + light)
                turn_off_light(light)
                return

            if self.target == "wiki_search":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                wiki_text = str(message['wikitext'])
                wiki_search(wiki_text)
                return

            if self.target == "mavs_game":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                ask_mavs_game()
                return

            if self.target == "whats_my_name":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                return

            if self.target == "who_am_i":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                return

            if self.target == "say_hello":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                flask_log.info(str(now_date) + " | " + str(now_time) + "Hello " + str(message['person']))
                return

            if self.target == "say_hello_two_people":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                flask_log.info(str(now_date) + " | " + str(now_time) + "Hello " + str(message['person1']) + " and " + str(message['person2']))
                return

            if self.target == "end_convo":
                now = dt.datetime.now()
                now_date = now.date()
                now_time = now.time()
                flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: " + "/convoresponse/COMMANDBEGUN: " + str(self.target))
                message = self.request.get_json()
                watson_delete_session(convo_id)
                time.sleep(2)
                play_sound("/home/pi/M.O.R.G./stt_files/listen_stop.wav")
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
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()

        flask_log.info(str(now_date) + " | " + str(now_time) + "-----FLASK----------: ACTION: " + str(action))
        if action == "greeting-hello" or action == "greeting-half-inquire" or action == "greeting-we-inquire" or action == "greeting-full-inquiry":
            thread_a = Compute(request.__copy__(), "any_greeting")
            thread_a.start()
            return jsonify({'action': 'any greeting', 'result': 'processing'})
        if action == "all-lights-on":
            thread_a = Compute(request.__copy__(), "all_lights_on")
            thread_a.start()
            return jsonify({'action': 'all lights on', 'result': 'processing'})
        if action == "all-lights-off":
            thread_a = Compute(request.__copy__(), "all_lights_off")
            thread_a.start()
            return jsonify({'action': 'all lights off', 'result': 'processing'})
        if action == "turn-on-light":
            thread_a = Compute(request.__copy__(), "light_on")
            thread_a.start()
            return jsonify({'action': 'one light on', 'result': 'processing'})
        if action == "turn-off-light":
            thread_a = Compute(request.__copy__(), "light_off")
            thread_a.start()
            return jsonify({'action': 'one light off', 'result': 'processing'})
        if action == "wiki-response":
            thread_a = Compute(request.__copy__(), "wiki_search")
            thread_a.start()
            return jsonify({'action': 'wiki', 'result': 'processing'})
        if action == "mavs-game":
            thread_a = Compute(request.__copy__(), "mavs_game")
            thread_a.start()
            return jsonify({'action': 'mavs', 'result': 'processing'})
        if action == "whats-my-name":
            thread_a = Compute(request.__copy__(), "whats_my_name")
            thread_a.start()
            return jsonify({'action': 'whats my name', 'result': 'processing'})
        if action == "who-am-i":
            thread_a = Compute(request.__copy__(), "who_am_i")
            thread_a.start()
            return jsonify({'action': 'who am i', 'result': 'processing'})
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
            thread_a = Compute(request.__copy__(), "repeat_that")
            thread_a.start()
            return jsonify({'action': 'action not found', 'result': 'repeating'})
        if action == "anything-else":
            thread_a = Compute(request.__copy__(), "anything_else")
            thread_a.start()
            return jsonify({'action': 'anything else', 'result': 'repeating'})
        if action == "end-convo":
            thread_a = Compute(request.__copy__(), "end_convo")
            thread_a.start()
            return jsonify({'action': 'end convo', 'result': 'ended'})
        else:
            return jsonify({'action': 'action not found', 'result': 'not processing'})


    app.run()

except KeyboardInterrupt:
    exit()
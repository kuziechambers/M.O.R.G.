import os
import sys
from os import path
import datetime as dt
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1, SpeechToTextV1
from ibm_watson.websocket import SynthesizeCallback, RecognizeCallback, AudioSource
from events_sound import play_sound
from logger import flask_log
import pyaudio


##########################################################
################## TEXT-TO-SPEECH CLASS ##################
##########################################################
tts_api_key = "xd5WDO7vtjDEf5v9jzmYbdbRG6zLm2AK4PBmk8y6PxCV"
tts_wss_url = "wss://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba47dae7-3648-4a3c-9df9-679f789c4fd2"

tts_authenticator = IAMAuthenticator(tts_api_key)
tts = TextToSpeechV1(authenticator=tts_authenticator)
tts.set_service_url(tts_wss_url)

f_path = "/Users/kuziechambers/PyCharmProjects/M.O.R.G./stt_files/listening_b.wav"

class TTSCallback(SynthesizeCallback):
    def __init__(self, file_path):
        SynthesizeCallback.__init__(self)
        self.file_path = file_path
        if path.exists(self.file_path):
            os.remove(self.file_path)
        self.fd = open(self.file_path, 'ab')

    def on_connected(self):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----TTS------------: Connection was successful')

    def on_error(self, error):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----TTS------------: Error received: {}'.format(error))

    def on_timing_information(self, timing_information):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + timing_information)

    def on_audio_stream(self, audio_stream):
        self.fd.write(audio_stream)

    def on_close(self):
        self.fd.close()
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----TTS------------: Done synthesizing. Closing the connection')

def synthesize_wss(text, sound_path):
    new_text = '<speak><prosody pitch="-3st"><prosody rate="130">' + text + '</prosody></prosody></speak>'
    my_callback = TTSCallback(sound_path)
    tts.synthesize_using_websocket(new_text,
                                   my_callback,
                                   accept='audio/wav',
                                   voice='en-GB_JamesV3Voice')



# synthesize_wss("Will that be all for now.", f_path)
# fx_to_file(f_path, "/Users/kuziechambers/PyCharmProjects/M.O.R.G./stt_files/willthatbeall.wav")





##########################################################
################## SPEECH-TO-TEXT CLASS ##################
##########################################################
try:
    from Queue import Queue, Full
except ImportError:
    from queue import Queue, Full

stt_api_key = "k1m0jszudJwIwrpwtUAT50OHK0E8Kdbi6WR5NpPVrkbI"
stt_url = "wss://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/74a3c1c6-e299-40a4-8c20-84da0ea7c27f"

stt_authenticator = IAMAuthenticator(stt_api_key)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(stt_url)

CHUNK = 3 * 1024
BUF_MAX_SIZE = CHUNK * 10
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


# define callback for the speech to text service
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)
        self.transcript = "none"

    def on_transcription(self, transcript):
        self.transcript = transcript

    def get_transcript(self):
        return self.transcript

    def on_connected(self):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----STT------------: Connection was successful')

    def on_error(self, error):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----STT------------: Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----STT------------: Inactivity timeout: {}'.format(error))

    def on_listening(self):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + '-----STT------------: Service is listening')
        play_sound("/Users/kuziechambers/PyCharmProjects/M.O.R.G./stt_files/listen_wake.wav")

    def on_hypothesis(self, hypothesis):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: " + hypothesis)

    # def on_data(self, data):
    #     print(data)

    def on_close(self):
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: Connection closed")


class WebsocketThreadClass:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            try:
                print("")
            except:
                print("Recognize finished.")
            return



# this function will initiate the recognize service and pass in the AudioSource
# def recognize_using_websocket(*args):
#     mycallback = MyRecognizeCallback()
#     stt.recognize_using_websocket(audio=audio_source,
#                                   content_type='audio/l16; rate=44100',
#                                   recognize_callback=mycallback,
#                                   interim_results=True,
#                                   low_latency=True,
#                                   inactivity_timeout=2,
#                                   model='en-US_BroadbandModel',
#                                   customization_id='139e688f-f2bc-47a5-a670-8e25294580ff'
#                                   )
#     return mycallback.get_transcript()


def pyaudio_callback(in_data, frame_count, time_info, status):

    # Create an instance of AudioSource
    # instantiate pyaudio

    try:
        q.put(in_data)
        #print(in_data)
    except Full:
        pass  # discard
    return None, pyaudio.paContinue


# noinspection PyTypeChecker
def stt_listen_and_recognize():

    global q
    q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))

    with q.mutex:
        q.queue.clear()

    audio = pyaudio.PyAudio()
    audio_source = AudioSource(q, True, True)
    # open stream using callback
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=3,
        frames_per_buffer=CHUNK,
        stream_callback=pyaudio_callback,
        start=False
    )
    try:
        stream.start_stream()
    except:
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: " + sys.exc_info())

    mycallback = MyRecognizeCallback()
    stt.recognize_using_websocket(audio=audio_source,
                                  content_type='audio/l16; rate=44100',
                                  background_audio_suppression=0.2,
                                  recognize_callback=mycallback,
                                  interim_results=True,
                                  low_latency=False,
                                  inactivity_timeout=3,
                                  model='en-US_BroadbandModel',
                                  customization_id='139e688f-f2bc-47a5-a670-8e25294580ff'
                                  )
    transcript = mycallback.get_transcript()
    try:
        text_output = transcript[0]
        text_output = text_output['transcript']
        stream.stop_stream()
        stream.close()
        audio.terminate()
        #audio_source.completed_recording()
    except:
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: " + str(transcript))
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: " + str(sys.exc_info()))
        text_output = "no audio"
        stream.stop_stream()
        stream.close()
        audio.terminate()

    return text_output







import datetime as dt
import json
import os
import sys
from os import path

import sounddevice as sd
import wikipedia
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2, SpeechToTextV1, TextToSpeechV1
from scipy.io.wavfile import write

from events_sound import fx_to_file, play_fx_file
from events_text import send_text
from events_wss import TTSCallback  # , stt_listen_and_recognize
from logger import flask_log
from utils import play_sound

# KEYS & URLS
WATSON_API_KEY = os.getenv("WATSON_API_KEY")
WATSON_URL = os.getenv("WATSON_URL")
WATSON_ID = os.getenv("WATSON_ID")
STT_API_KEY = os.getenv("STT_API_KEY")
STT_URL = os.getenv("STT_URL")
TTS_API_KEY = os.getenv("TTS_API_KEY")
TTS_WSS_URL = os.getenv("TTS_WSS_URL")



# INIT AUTHENTICATORS
authenticator = IAMAuthenticator(WATSON_API_KEY)
assistant = AssistantV2(version='2020-04-01',authenticator=authenticator)
assistant.set_service_url(WATSON_URL)

stt_authenticator = IAMAuthenticator(STT_API_KEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

tts_authenticator = IAMAuthenticator(TTS_API_KEY)
tts = TextToSpeechV1(authenticator=tts_authenticator)
tts.set_service_url(TTS_WSS_URL)

#
# Functions are in order of: TTS functions, STT functions, Watson functions
#


# TTS FUNCTIONS
def tts_read_play_ssml(ssml_file, filename):
    """
    Read ssml file, TTS, save as wav file, then play
    :param ssml_file:
    :param filename:
    """
    ssml_path = "/Users/kuchambers/PycharmProjects/M.O.R.G./ssml_files/" + ssml_file
    sound_path = "/Users/kuchambers/PycharmProjects/M.O.R.G./sounds/" + filename + "_nofx.wav"
    with open(ssml_path, 'r') as f:
        text = f.read()
    my_callback = TTSCallback(sound_path)
    tts.synthesize_using_websocket(text,
                                   my_callback,
                                   accept='audio/wav',
                                   voice='en-GB_JamesV3Voice')
    play_sound(sound_path)


def tts_transcribe_play(text):
    """
    Read text param, add prosody, TTS, apply FX, then play
    :param text:
    """
    inpath = "/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response.wav"
    outpath = "/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response_fx.wav"
    pro_text = '<speak><prosody pitch="-3st"><prosody rate="130">' + text + '</prosody></prosody></speak>'
    my_callback = TTSCallback(inpath)
    tts.synthesize_using_websocket(pro_text,
                                   my_callback,
                                   accept='audio/wav',
                                   voice='en-GB_JamesV3Voice')
    fx_to_file(inpath, outpath)
    play_fx_file()


def tts_transcribe(text):
    """
    Read text param, TTS, save to _temp_response.wav
    :param text:
    """
    sound_path = "/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response.wav"
    pro_text = prosody_on_text(text)
    my_callback = TTSCallback(sound_path)
    tts.synthesize_using_websocket(pro_text,
                                   my_callback,
                                   accept='audio/wav',
                                   voice='en-GB_JamesV3Voice')


def prosody_on_text(text):
    """
    Add proper prosody on the TTS text
    :param text:
    :return: str(new_text)
    """
    new_text = '<speak><prosody pitch="-3st"><prosody rate="130">' + text + '</prosody></prosody></speak>'
    return new_text


# STT FUNCTIONS
def stt_recognize():
    """
    Grab speech from _spoken_input.wav file, STT, return text_output
    :return: str(text_output)
    """
    if path.exists("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav"):
        with open('/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav', 'rb') as audio_file:
            transcript = stt.recognize(
                audio=audio_file,
                content_type='audio/wav',
                model='en-US_BroadbandModel',
                continuous=True,
                customization_id='139e688f-f2bc-47a5-a670-8e25294580ff'
            ).get_result()

        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + str(transcript))

        text_output = transcript['results'][0]['alternatives'][0]['transcript']
        text_output = text_output.strip()

        os.remove("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav")
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + text_output)
        return str(text_output)


def start_recording():
    """

    """
    fs = 44100  # Sample rate
    seconds = 8  # Duration of recording
    # for airpods
    sd.default.channels = 1, 2
    # for mac
    # sd.default.channels = 2
    recording = sd.rec(int(seconds * fs), samplerate=fs)
    now = dt.datetime.now()
    now_date = now.date()
    now_time = now.time()
    flask_log.info(str(now_date) + " | " + str(now_time) + "Starting recording...")
    send_text("Starting recording...")
    sd.wait()  # Wait until recording is finished
    write('/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav', fs, recording)  # Save as WAV file
    if path.exists("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav"):
        send_text("Recording stopped, audio file saved./n/n-M.O.R.G.")
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "Recording stopped, audio file saved.")
    if not path.exists("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_spoken_input.wav"):
        send_text("Recording stopped, audio file NOT saved./n/n-M.O.R.G.")
        now = dt.datetime.now()
        now_date = now.date()
        now_time = now.time()
        flask_log.info(str(now_date) + " | " + str(now_time) + "Recording stopped, audio file NOT saved.")


# WATSON FUNCTIONS
def watson_create_session():
    response = assistant.create_session(assistant_id=WATSON_ID).get_result()
    sesh_id = response['session_id']
    return sesh_id


def watson_init_session():
    response = assistant.create_session(
        assistant_id=WATSON_ID
    ).get_result()
    sesh_id = response['session_id']
    # Create IBM Watson Assistant session
    return sesh_id


def watson_delete_session(sesh_id):
    assistant.set_service_url(WATSON_URL)
    response = assistant.delete_session(
        assistant_id=WATSON_ID,
        session_id=sesh_id
    ).get_result()
    return json.dumps(response, indent=2)


# # noinspection PyTypeChecker
# def stt_watson_tts(sesh_id):
#
#     # Initialize and transcribe IBM Speech-to-Text
#     stt_text = stt_listen_and_recognize()
#     now = dt.datetime.now()
#     now_date = now.date()
#     now_time = now.time()
#     flask_log.info(str(now_date) + " | " + str(now_time) + "-----STT------------: " + stt_text)
#     if stt_text == "no audio":
#         return sesh_id
#
#     # Send request to IBM Watson Assistant session
#     response = assistant.message(
#         assistant_id=watson_id,
#         session_id=sesh_id,
#         input={
#             'message_type': 'text',
#             'text': stt_text
#         }
#     ).get_result()
#     message = json.dumps(response)
#     message = json.loads(message)
#     now = dt.datetime.now()
#     now_date = now.date()
#     now_time = now.time()
#     flask_log.info(str(now_date) + " | " + str(now_time) + "-----WATSON---------: " + str(message))
#     response_type = message['output']['generic'][0]['response_type']
#     if response_type == "suggestion":
#         suggestions = [message['output']['generic'][0]['suggestions'][0]['label'].strip("-"),
#                        message['output']['generic'][0]['suggestions'][1]['label'].strip("-")]
#
#         #watson_response = "Apologies, did you say " + suggestions[0] + " or " + suggestions[1] + "?"
#         tts_transcribe_play("Apologies, did you say " + suggestions[0] + " or " + suggestions[1] + "?")
#         stt_listen_and_recognize()
#         return sesh_id
#
#     else:
#         try:
#             watson_response = message['output']['generic'][0]['text']
#         except:
#             now = dt.datetime.now()
#             now_date = now.date()
#             now_time = now.time()
#             flask_log.info(str(now_date) + " | " + str(now_time) + message)
#             print(sys.exc_info())
#             watson_response = "Apologies sir, I didn't understand."
#
#     now = dt.datetime.now()
#     now_date = now.date()
#     now_time = now.time()
#     flask_log.info(str(now_date) + " | " + str(now_time) + "-----WATSON---------: " + watson_response)
#     watson_response = prosody_on_text(str(watson_response))
#
#
#     # Initialize and transcribe IBM Text-to-Speech
#     sound_path = "/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response.wav"
#     my_callback = TTSCallback(sound_path)
#     tts.synthesize_using_websocket(watson_response,
#                                    my_callback,
#                                    accept='audio/wav',
#                                    voice='en-GB_JamesV3Voice')
#
#     fx_to_file(sound_path, "/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response_fx.wav")
#     play_fx_file()
#
#     return sesh_id


def wiki_search(wiki_text):
    now = dt.datetime.now()
    now_date = now.date()
    now_time = now.time()
    flask_log.info(str(now_date) + " | " + str(now_time) + "-----WIKI-----------: " + wiki_text)
    suggestion = wikipedia.suggest(wiki_text)
    now = dt.datetime.now()
    now_date = now.date()
    now_time = now.time()
    flask_log.info(str(now_date) + " | " + str(now_time) + "-----WIKI-----------: " + str(suggestion))
    if suggestion is None:
        try:
            summary = wikipedia.summary(wiki_text, sentences=2)
        except wikipedia.exceptions.DisambiguationError:
            summary = "My apologies, it appears the word " + wiki_text + " is either too disambiguous for my wiki search or it doesn't exist. Ask in another way."
    if suggestion is not None:
        summary = wikipedia.summary(suggestion, sentences=2)

    now = dt.datetime.now()
    now_date = now.date()
    now_time = now.time()
    flask_log.info(str(now_date) + " | " + str(now_time) + "-----WIKI-----------: " + summary)
    slow_summary = '<speak><prosody pitch="-1st"><prosody rate="130">' + summary + '</prosody></prosody></speak>'
    tts_transcribe(slow_summary)
    fx_to_file("/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response.wav","/Users/kuchambers/PycharmProjects/M.O.R.G./stt_files/_temp_response_fx.wav")
    play_fx_file()

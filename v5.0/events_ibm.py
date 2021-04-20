import json
import os
import sys
from os import path
from statistics import mean
from ibm_watson import AssistantV2, SpeechToTextV1, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write
from events_text import send_text
from ibm_watson.websocket import SynthesizeCallback
from events_sound import fx_to_file, record_to_file, play_fx_file

class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)

    def on_audio_stream(self, audio_stream):
        return audio_stream

    def on_data(self, data):
        return data


# KEYS & URLS
watson_api_key = "Oam6wIYU5kg59U3JJiOGUztOTSoF1lk0RMXgvVyOiSCW"
watson_url = "https://api.us-south.assistant.watson.cloud.ibm.com/instances/7ddf978f-efef-40d0-a79c-ac0d9d58a377"
watson_id = "3f934fcc-26e7-4859-9ca8-9295241370c2"
stt_api_key = "k1m0jszudJwIwrpwtUAT50OHK0E8Kdbi6WR5NpPVrkbI"
stt_url = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/74a3c1c6-e299-40a4-8c20-84da0ea7c27f"
tts_api_key = 'xd5WDO7vtjDEf5v9jzmYbdbRG6zLm2AK4PBmk8y6PxCV'
tts_api_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba47dae7-3648-4a3c-9df9-679f789c4fd2'

# INIT AUTHENTICATORS
authenticator = IAMAuthenticator(watson_api_key)
assistant = AssistantV2(version='2020-04-01',authenticator=authenticator)
assistant.set_service_url(watson_url)

stt_authenticator = IAMAuthenticator(stt_api_key)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(stt_url)

tts_authenticator = IAMAuthenticator(tts_api_key)
tts = TextToSpeechV1(authenticator=tts_authenticator)
tts.set_service_url(tts_api_url)

#
# Functions are in order of: TTS functions, STT functions, Watson functions
#

# TTS FUNCTIONS
def tts_play(ssml_file, filename):
    ssml_path = "/hopme/pi/M.O.R.G./ssml_files/" + ssml_file
    sound_path = "/hopme/pi/M.O.R.G./ssml_files/" + filename + ".wav"
    with open(ssml_path, 'r') as f:
        text = f.read()
    with open(sound_path, 'wb') as audio_file:
        audio_file.write(
            tts.synthesize(
                text,
                #voice='en-US_HenryV3Voice',
                #voice='en-US_KevinV3Voice',
                voice='en-GB_JamesV3Voice',# 'en-GB_JamesV3Voice' "en-US_MichaelVoice"
                accept='audio/wav'
            ).get_result().content)
    playsound(sound_path)

def play_response(text):
    sound_path = "/hopme/pi/M.O.R.G./stt_files/temp_response.wav"
    pro_text = '<speak><prosody pitch="-3st"><prosody rate="130">' + text + '</prosody></prosody></speak>'
    with open(sound_path, 'wb') as audio_file:
        audio_file.write(
            tts.synthesize(
                pro_text,
                #voice='en-US_HenryV3Voice',
                #voice='en-US_KevinV3Voice',
                voice='en-GB_JamesV3Voice',# 'en-GB_JamesV3Voice' "en-US_MichaelVoice"
                accept='audio/wav'
            ).get_result().content)
    fx_to_file()
    playsound("/hopme/pi/M.O.R.G./stt_files/temp_response_fx.wav")

def transcribe_response(text):
    sound_path = "/hopme/pi/M.O.R.G./stt_files/temp_response.wav"
    pro_text = '<speak><prosody pitch="-3st"><prosody rate="125">' + text + '</prosody></prosody></speak>'
    with open(sound_path, 'wb') as audio_file:
        audio_file.write(
            tts.synthesize(
                pro_text,
                #voice='en-US_HenryV3Voice',
                #voice='en-US_KevinV3Voice',
                voice='en-GB_JamesV3Voice',# 'en-GB_JamesV3Voice' "en-US_MichaelVoice"
                accept='audio/wav'
            ).get_result().content)
    playsound(sound_path)


def prosody_on_text(text):
    new_text = '<speak><prosody pitch="-3st"><prosody rate="130">' + text + '</prosody></prosody></speak>'
    return new_text




# STT FUNCTIONS
def stt_transcribe():
   if path.exists("/hopme/pi/M.O.R.G./stt_files/spoken_input.wav"):
      with open('/hopme/pi/M.O.R.G./stt_files/spoken_input.wav', 'rb') as audio_file:
         transcript = stt.recognize(audio=audio_file, content_type='audio/wav', model='en-US_BroadbandModel', continuous=True, customization_id='139e688f-f2bc-47a5-a670-8e25294580ff').get_result()
         #transcript = stt.recognize(audio=audio_file, content_type='audio/wav', model='en-US_BroadbandModel', continuous=True).get_result()
      print(transcript)

      text_output = transcript['results'][0]['alternatives'][0]['transcript']
      text_output = text_output.strip()

      os.remove("/hopme/pi/M.O.R.G./stt_files/spoken_input.wav")
      print(text_output)
      return str(text_output)

def start_recording():
   fs = 44100  # Sample rate
   seconds = 8  # Duration of recording

   # for airpods
   sd.default.channels = 1,2
   # for mac
   #sd.default.channels = 2

   recording = sd.rec(int(seconds * fs), samplerate=fs)

   print("Starting recording...")
   send_text("Starting recording...")
   sd.wait()  # Wait until recording is finished
   write('/hopme/pi/M.O.R.G./stt_files/spoken_input.wav', fs, recording)  # Save as WAV file
   if path.exists("/hopme/pi/M.O.R.G./stt_files/spoken_input.wav"):
      send_text("Recording stopped, audio file saved./n/n-M.O.R.G.")
      print("Recording stopped, audio file saved.")
   if not path.exists("/hopme/pi/M.O.R.G./stt_files/spoken_input.wav"):
      send_text("Recording stopped, audio file NOT saved./n/n-M.O.R.G.")
      print("Recording stopped, audio file NOT saved.")




# WATSON FUNCTIONS
def watson_create_session():
    response = assistant.create_session(assistant_id=watson_id).get_result()
    sesh_id = response['session_id']
    return sesh_id

def init_watson_session():
    response = assistant.create_session(
        assistant_id=watson_id
    ).get_result()
    sesh_id = response['session_id']
    # Create IBM Watson Assistant session
    return sesh_id

# noinspection PyTypeChecker
def send_whole_watson_request(sesh_id):

    # Initialize and transcribe IBM Speech-to-Text
    with open('/hopme/pi/M.O.R.G./stt_files/spoken_input.wav', 'rb') as audio_file:
        transcript = stt.recognize(audio=audio_file,
                                   content_type='audio/wav',
                                   model='en-US_BroadbandModel',
                                   continuous=True,
                                   interim_results=True,
                                   low_latency=True,
                                   customization_id='139e688f-f2bc-47a5-a670-8e25294580ff').get_result()
    os.remove("/hopme/pi/M.O.R.G./stt_files/spoken_input.wav")
    results = transcript['results']
    transcripts = []
    confidences = []

    for final in results:
        for key, value in final.items():
            if key == 'alternatives':
                for item in value:
                    for k, v in item.items():
                        if k == 'transcript':
                            transcripts.append(v)
                        if k == 'confidence':
                            confidences.append(v)
    stt_text = ''.join(transcripts).strip()
    confidence = mean(confidences)
    print("Text: '" + stt_text + "' | Confidence: " + str(confidence))
    print()

    # Send request to IBM Watson Assistant session
    response = assistant.message(
        assistant_id=watson_id,
        session_id=sesh_id,
        input={
            'message_type': 'text',
            'text': stt_text
        }
    ).get_result()
    message = json.dumps(response)
    message = json.loads(message)
    print(message)
    response_type = message['output']['generic'][0]['response_type']
    if response_type == "suggestion":
        suggestions = [message['output']['generic'][0]['suggestions'][0]['label'].strip("-"),
                       message['output']['generic'][0]['suggestions'][1]['label'].strip("-")]

        #watson_response = "Apologies, did you say " + suggestions[0] + " or " + suggestions[1] + "?"
        play_response("Apologies, did you say " + suggestions[0] + " or " + suggestions[1] + "?")
        record_to_file('/hopme/pi/M.O.R.G./stt_files/spoken_input.wav')
        return sesh_id

    else:
        try:
            watson_response = message['output']['generic'][0]['text']
        except:
            print(message)
            print(sys.exc_info())
            watson_response = "Apologies sir, I didn't understand."

    watson_response = prosody_on_text(str(watson_response))
    print(watson_response)

    # Initialize and transcribe IBM Text-to-Speech
    sound_path = "/hopme/pi/M.O.R.G./stt_files/temp_response.wav"
    with open(sound_path, 'wb') as audio_file:
        audio_file.write(
            tts.synthesize(
                watson_response,
                # voice='en-US_HenryV3Voice',
                # voice='en-US_KevinV3Voice',
                voice='en-GB_JamesV3Voice',  # 'en-GB_JamesV3Voice' "en-US_MichaelVoice"
                accept='audio/wav',
            ).get_result().content)

    fx_to_file()
    play_fx_file()

    return sesh_id

def watson_delete_session(sesh_id):
    assistant.set_service_url(watson_url)
    response = assistant.delete_session(
        assistant_id=watson_id,
        session_id=sesh_id
    ).get_result()

    return json.dumps(response, indent=2)

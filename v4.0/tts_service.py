from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from constants_sound import sound_play

s_heressomemusic = "Welcome home sir, I presume you’re having a wonderful day. Here’s some music to keep it going."

ibm_api_key = 'xd5WDO7vtjDEf5v9jzmYbdbRG6zLm2AK4PBmk8y6PxCV'
ibm_api_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba47dae7-3648-4a3c-9df9-679f789c4fd2'

authenticator = IAMAuthenticator(ibm_api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(ibm_api_url)

def tts_play(sound_string, filename):
    full_path = "/Users/kuziechambers/PycharmProjects/M.O.R.G./v4.0/" + filename
    with open(full_path, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                sound_string,
                voice='en-GB_JamesV3Voice',
                accept='audio/wav'
            ).get_result().content)

    sound_play(full_path)

tts_play(s_heressomemusic, "heressomemusic")




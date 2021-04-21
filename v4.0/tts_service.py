from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from constants_sound import play_sound


#text = [line.replace('\n','') for line in text]
#text = ''.join(str(line) for line in text)


ibm_api_key = 'xd5WDO7vtjDEf5v9jzmYbdbRG6zLm2AK4PBmk8y6PxCV'
ibm_api_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/ba47dae7-3648-4a3c-9df9-679f789c4fd2'

authenticator = IAMAuthenticator(ibm_api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(ibm_api_url)

voices = text_to_speech.list_voices().get_result()
#print(json.dumps(voices, indent=2))

def tts_play(ssml_file, filename):
    ssml_path = "/Users/kuziechambers/PycharmProjects/M.O.R.G./ssml_files/" + ssml_file
    sound_path = "/Users/kuziechambers/PycharmProjects/M.O.R.G./ssml_files/" + filename + ".wav"

    with open(ssml_path, 'r') as f:
        text = f.read()

    with open(sound_path, 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                text,
                #voice='en-US_HenryV3Voice',
                #voice='en-US_KevinV3Voice',
                voice='en-GB_JamesV3Voice',# 'en-GB_JamesV3Voice' "en-US_MichaelVoice"
                accept='audio/wav'
            ).get_result().content)

    #play_sound(sound_path)


tts_play('x_afternoonwelcomeback1', 'afternoonwelcomeback1')
#tts_read_play_ssml("x_morningproductiveday", "morningproductiveday")




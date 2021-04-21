import sys
import os
from os import path
from events_ibm import stt_watson_tts, watson_init_session, watson_delete_session
from events_sound import fx_to_file, play_fx_file

#print(sounddevice.query_devices())

convo_id = watson_init_session()
new_session_id = None

while True:
    try:
        if path.exists('/home/pi/M.O.R.G./stt_files/_spoken_input.wav'):
            # noinspection PyUnboundLocalVariable
            if new_session_id is not None:
                stt_watson_tts(convo_id)
            else:
                new_session_id = stt_watson_tts(convo_id)

    except KeyboardInterrupt:
        if path.exists('/home/pi/M.O.R.G./stt_files/_spoken_input.wav'):
            os.remove('/home/pi/M.O.R.G./stt_files/_spoken_input.wav')
        exit()
    # except:
    #     print(sys.exc_info())
    #     if path.exists('/home/pi/M.O.R.G./stt_files/_spoken_input.wav'):
    #         os.remove('/home/pi/M.O.R.G./stt_files/_spoken_input.wav')

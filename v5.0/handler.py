import sys
import os
from os import path
from events_ibm import send_whole_watson_request, init_watson_session, watson_delete_session
from events_sound import fx_to_file, play_fx_file

#print(sounddevice.query_devices())

convo_id = init_watson_session()
new_session_id = None

while True:
    try:
        if path.exists('/home/pi/M.O.R.G./stt_files/spoken_input.wav'):
            # noinspection PyUnboundLocalVariable
            if new_session_id is not None:
                send_whole_watson_request(convo_id)
            else:
                new_session_id = send_whole_watson_request(convo_id)

    except KeyboardInterrupt:
        if path.exists('/home/pi/M.O.R.G./stt_files/spoken_input.wav'):
            os.remove('/home/pi/M.O.R.G./stt_files/spoken_input.wav')
        exit()
    # except:
    #     print(sys.exc_info())
    #     if path.exists('/home/pi/M.O.R.G./stt_files/spoken_input.wav'):
    #         os.remove('/home/pi/M.O.R.G./stt_files/spoken_input.wav')

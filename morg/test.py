from threading import Thread

import pyaudio

from events_ibm import tts_read_play_ssml
from events_sound import fx_to_file, play_fx_file
from events_weather import get_rain

tts_read_play_ssml("x_weatherreport_1", "weatherreport1")
tts_read_play_ssml("x_weatherreport_2", "weatherreport2")
tts_read_play_ssml("x_weatherreport_3", "weatherreport3")


#tts_read_play_ssml("x_morningwelcomeback2", "morningwelcomeback2")
#fx_to_file("/Users/kuchambers/PycharmProjects/M.O.R.G./ssml_files/morninghadfun.wav", "/Users/kuchambers/PycharmProjects/M.O.R.G./ssml_files/morninghadfun.wav")

# p = pyaudio.PyAudio()
#
# print(p.get_default_input_device_info())
# print()
# print()
# print()
# print()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))
#
# print()
# print()
# print()
# print()
# for i in range(p.get_host_api_count()):
#     print(p.get_host_api_info_by_index(i))

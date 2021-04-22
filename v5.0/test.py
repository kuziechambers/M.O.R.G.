from threading import Thread

from events_sound import play_sound
import pyaudio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import concurrent.futures
import pyaudio


p = pyaudio.PyAudio()
print(p.get_default_input_device_info())
print()
print()
print()
print()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

print()
print()
print()
print()
for i in range(p.get_host_api_count()):
    print(p.get_host_api_info_by_index(i))

mics = []
for device in range(self.p.get_device_count()):
    if self.valid_test(device):
        mics.append(device)
if len(mics) == 0:
    print("no microphone devices found!")
else:
    print("found %d microphone devices: %s" % (len(mics), mics))

print()
print()
print()
print()
print(mics)



from threading import Thread

from events_sound import play_sound
import pyaudio
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import concurrent.futures
import pyaudio

def valid_input_devices(py):
    """
    See which devices can be opened for microphone input.
    call this when no PyAudio object is loaded.
    """
    mics = []
    for device in range(py.get_device_count()):
        if py.is_format_supported(device):
            mics.append(device)
    if len(mics) == 0:
        print("no microphone devices found!")
    else:
        print("found %d microphone devices: %s" % (len(mics), mics))
    return mics


p = pyaudio.PyAudio()

print()
print()
print()
print()
valid_input_devices(p)


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










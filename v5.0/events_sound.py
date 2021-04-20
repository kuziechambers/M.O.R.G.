import os
from os import path
from sys import byteorder
from array import array
from struct import pack
from events_text import send_text
import pyaudio
import wave
from pysndfx import AudioEffectsChain
from constants import play_sound
import soundfile as sf
#from events_ibm import prosody_on_text

THRESHOLD = 500
CHUNK_SIZE = 2*1024
FORMAT = pyaudio.paInt16
RATE = 44100

def is_silent(snd_data):
    # Returns 'True' if below the 'silent' threshold
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    # Average the volume out
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    #Trim the blank spots at the start and end
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    #snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    # Add silence to the start and end of 'snd_data' of length 'seconds' (float)
    silence = [0] * int(seconds * RATE)
    r = array('h', silence)
    r.extend(snd_data)
    r.extend(silence)
    return r

def record():
    """
    Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure VLC et al can play
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(output_path):
    # Records from the microphone and outputs the resulting data to 'path'
    if path.exists(output_path):
        os.remove(output_path)
    #send_text("Listening...\n\n-M.O.R.G.")
    play_sound('/home/pi/M.O.R.G./stt_files/listening.wav')
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)
    wf = wave.open(output_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
    #send_text("Stopped Listening.\n\n-M.O.R.G.")
    print(".wav File saved.")

def record_to_file_wosir(output_path):
    # Records from the microphone and outputs the resulting data to 'path'
    if path.exists(output_path):
        os.remove(output_path)
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)
    wf = wave.open(output_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
    print(".wav File saved.")

def fx_to_file():
    fx = (
        AudioEffectsChain()
            .highshelf(gain=5)
            .reverb(room_scale=10)
            .phaser(delay=0.5)
        # .lowshelf()
    )

    infile = '/Users/kuziechambers/PyCharmProjects/M.O.R.G./stt_files/temp_response.wav'
    outfile = '/Users/kuziechambers/PyCharmProjects/M.O.R.G./stt_files/temp_response_fx.wav'
    fx(infile, outfile)

    # Read wav with dtype= 'int16'
    # data, samplerate = sf.read(infile, dtype='int16')
    # x = fx(x)
    # x = fx(infile)
    # # Write 'int16'-signal and read with default
    # sf.write(outfile, x, Fs)



def play_fx_file():
    play_sound('/home/pi/M.O.R.G./stt_files/temp_response_fx.wav')

fx_to_file()

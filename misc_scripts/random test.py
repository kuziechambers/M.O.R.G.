import random
import pygame
import simpleaudio as audio

s_saturdaybackinblack = "/home/pi/Documents/MORGsounds/saturdaybackinblack.wav"
s_saturdayhighwaytohell = "/home/pi/Documents/MORGsounds/saturdayhighwaytohell.wav"
s_chiquita = "/home/pi/Documents/MORGsounds/chiquita2.wav"
s_whatspoppin = "/home/pi/Documents/MORGsounds/whatspoppin.wav"

phrases = [s_saturdaybackinblack, s_saturdayhighwaytohell]
phrasez = [s_chiquita, s_whatspoppin]

group = [phrases, phrasez]

rint1 = random.randint(0,1)
path1 = group[rint1]
print(path1)

rint = random.randint(0,1)
path = path1[rint]
print(path)

#audio.WaveObject.from_wave_file(s_wake2).play().wait_done()
audio.WaveObject.from_wave_file(path).play().wait_done()

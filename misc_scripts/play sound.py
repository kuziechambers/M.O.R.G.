



# import simpleaudio as sa
# 
# filename = 'myfile.wav'
# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done()  # Wait until sound has finished playing


# 
# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load("/home/pi/Documents/MORGsounds(wav)/welcomehomemrchambers.wav")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue



# from playsound import playsound
# 
# playsound('/home/pi/Documents/MORGsounds(wav)/welcomehomemrchambers.wav')


# import pygame
# 
# pygame.mixer.init()
# pygame.mixer.music.load("/home/pi/Downloads/Welcome home sir.mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
# 
# pygame.mixer.music.load("/home/pi/Downloads/ACDC - Back In Black (Official Video).mp3")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
# 
# 
#



import simpleaudio as sa

filename = "/home/pi/Documents/MORGsounds/welcomehomemrchambers1.wav"
sa.WaveObject.from_wave_file(filename).play().wait_done()
#play_obj = wave_obj.play()
#play_obj.wait_done()  # Wait until sound has finished playing



# from openal import *
# import time
# 
# 
# source = oalOpen('/home/pi/Documents/MORGsounds(wav)/welcomehomemrchambers.wav')
# 
# 
# source.play()
# 
# while source.get_state() == AL_PLAYING:
#     # wait until the file is done playing
#     time.sleep(1)
# 
# oalQuit()



# 
# import random
# import pygame
# 
# 
# morningphrases = ["/home/pi/Documents/MORGsounds(wav)/welcomehomemrchambers.mp3",
#                   "/home/pi/Downloads/highwaytohell.mp3"]
# 
# rint = random.randint(0,0)
# path = morningphrases[rint]
#             
# pygame.init()
# sound = pygame.mixer.Sound('/home/pi/Documents/MORGsounds(wav)/welcomehomemrchambers.wav')
# sound.play()
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
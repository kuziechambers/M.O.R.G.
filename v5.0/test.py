import wikipedia
from events_ibm import transcribe_response
from events_sound import fx_to_file
from events_weather import get_rain, weather_update, get_weekend_temp

#print(get_rain())
from datetime import datetime
date_string = '00:00:00'

# r_time = datetime.strptime(date_string, '%H:%M:%S')
# time_string = str(r_time.strftime("%I:%M %p"))
#
# if time_string[:1] == "0":
#     date_P = time_string[1:2] + time_string[-2:]
# if time_string[:1] != "0":
#     date_P = time_string[0:2] + time_string[-2:]
#
# if date_P == "12AM":
#     date_P = "Midnight"
# print(date_P)

#weather_update()

transcribe_response("Anything else?")
fx_to_file()

# text = "nffl"
#
# suggestion = wikipedia.suggest("iron man")
# print(suggestion)
# print(wikipedia.summary(suggestion, sentences=3))

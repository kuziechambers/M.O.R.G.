from datetime import datetime
from events_ibm import tts_transcribe_play

def percent_to_float(x):
    return float(x.strip('%'))/100

class SportsEvent:
    def __init__(self, game_date, game_time, game_opp, home_away):
        self.game_date = game_date
        self.game_time = game_time
        self.game_opp = game_opp
        self.home_away = home_away

    def get_game_date(self):
        return str(self.game_date)

    def get_game_time(self):
        return str(self.game_time)
    
    def get_game_opp(self):
        return str(self.game_opp)

    def get_home_away(self):
        return str(self.home_away)






today_date = str(datetime.today()).split(" ")
today_date = today_date[0]
print(today_date)

def get_mavs_game():
    mavs_game_dates_times = {"2021-04-24 19:30": ['Lakers', 'Home'],
                             "2021-04-26 21:00": ["Kings", "Away"],
                             "2021-04-27 20:30": ["Warriors", "Away"],
                             "2021-04-29 18:00": ["Pistons", "Away"],
                             "2021-05-01 20:00": ["Wizards", "Home"],
                             "2021-05-02 19:00": ["Kings", "Home"],
                             "2021-05-04 19:00": ["Heat", "Away"],
                             "2021-05-06 18:30": ["Nets", "Home"],
                             "2021-05-07 19:30": ["Cavs", "Home"],
                             "2021-05-09 18:00": ["Cavs", "Home"],
                             "2021-05-11 19:00": ["Grizzlies", "Home"],
                             "2021-05-12 20:00": ["Pelicans", "Home"],
                             "2021-05-14 20:00": ["Raptors", "Home"],
                             "2021-05-16 19:30": ["Timberwolves", "Home"]}
    found = False
    text = "none"
    for g_date_time, g_opp_location in mavs_game_dates_times.items():
        date_times = g_date_time.split(" ")
        if date_times[0] == today_date:
            d = datetime.strptime(date_times[1], "%H:%M")
            time_string = str(d.strftime("%I:%M %p"))
            rain = True
            if time_string[:1] == "0":
                date_P = time_string[1:2] + time_string[-2:]
            if time_string[:1] != "0":
                date_P = time_string[0:2] + time_string[-2:]
            if date_P == "12AM":
                date_P = "Midnight"
            todays_game = SportsEvent(date_times[0], date_P, g_opp_location[0], g_opp_location[1])
            if todays_game.get_home_away() == "Home":
                text = "The Mavs play tonight at home against the " + todays_game.get_game_opp() +\
                       ". The game begins around " + todays_game.get_game_time()
            if todays_game.get_home_away() == "Away":
                text = "The Mavs play tonight on the road against the " + todays_game.get_game_opp() + \
                       ". The game begins around " + todays_game.get_game_time()
            found = True
            return found, text

    if found is False:
        return found, text

def ask_mavs_game():
    mavs_game_dates_times = {"2021-04-24 19:30": ['Lakers', 'Home'],
                             "2021-04-26 21:00": ["Kings", "Away"],
                             "2021-04-27 20:30": ["Warriors", "Away"],
                             "2021-04-29 18:00": ["Pistons", "Away"],
                             "2021-05-01 20:00": ["Wizards", "Home"],
                             "2021-05-02 19:00": ["Kings", "Home"],
                             "2021-05-04 19:00": ["Heat", "Away"],
                             "2021-05-06 18:30": ["Nets", "Home"],
                             "2021-05-07 19:30": ["Cavs", "Home"],
                             "2021-05-09 18:00": ["Cavs", "Home"],
                             "2021-05-11 19:00": ["Grizzlies", "Home"],
                             "2021-05-12 20:00": ["Pelicans", "Home"],
                             "2021-05-14 20:00": ["Raptors", "Home"],
                             "2021-05-16 19:30": ["Timberwolves", "Home"]}
    found = False
    for g_date_time, g_opp_location in mavs_game_dates_times.items():
        date_times = g_date_time.split(" ")
        if date_times[0] == today_date:
            d = datetime.strptime(date_times[1], "%H:%M")
            time_string = str(d.strftime("%I:%M %p"))
            rain = True
            if time_string[:1] == "0":
                date_P = time_string[1:2] + time_string[-2:]
            if time_string[:1] != "0":
                date_P = time_string[0:2] + time_string[-2:]
            if date_P == "12AM":
                date_P = "Midnight"
            todays_game = SportsEvent(date_times[0], date_P, g_opp_location[0], g_opp_location[1])
            if todays_game.get_home_away() == "Home":
                text = "The Mavs play tonight at home against the " + todays_game.get_game_opp() +\
                       ". The game begins around " + todays_game.get_game_time()
            if todays_game.get_home_away() == "Away":
                text = "The Mavs play tonight on the road against the " + todays_game.get_game_opp() + \
                       ". The game begins around " + todays_game.get_game_time()
            tts_transcribe_play(text)
            found = True
            return

    if found is False:
        text = "The Mavs do not play tonight."
        print(text)
        tts_transcribe_play(text)



# url = "https://www.basketball-reference.com/teams/DAL/2021_games.html"
#
# #try:
# driver = webdriver.Chrome("/Users/kuziechambers/chromedriver")
# driver.set_window_size(200, 1000)
# driver.get(url)
# driver.implicitly_wait(5)
#
#
# table_div = driver.find_element_by_id("games")
# table_body = table_div.find_element_by_tag_name("tbody")
# table_rows = table_body.find_elements_by_tag_name("tr")
#
# player_names = []
# teams_list = []
# freqs_list = []
#
# for row in table_rows:
#     print(row)
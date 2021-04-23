import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as panda

def percent_to_float(x):
    return float(x.strip('%'))/100

class SportsEvent:
    def __init__(self, game_date, game_time, game_opp, home_away):
        self.game_date = game_date
        self.game_time = game_time
        self.game_opp = game_opp
        self.home_away = home_away

    def get_game_date(self):
        return self.game_date

    def get_game_time(self):
        return self.game_date
    
    def get_game_opp(self):
        return self.game_date

    def get_home_away(self):
        return self.home_away

                        


mavs_game_dates_times = {"2021-04-24 19:30" : ['Lakers','Home'],
                         "2021-04-26 21:00" : ["Kings","Away"],
                         "2021-04-27 20:30" : ["Warriors","Away"],
                         "2021-04-29 18:00" : ["Pistons","Away"],
                         "2021-05-01 20:00" : ["Wizards","Home"],
                         "2021-05-02 19:00" : ["Kings","Home"],
                         "2021-05-04 19:00" : ["Heat","Away"],
                         "2021-05-06 18:30" : ["Nets","Home"],
                         "2021-05-07 19:30" : ["Cavs","Home"],
                         "2021-05-09 18:00" : ["Cavs","Home"],
                         "2021-05-11 19:00" : ["Grizzlies","Home"],
                         "2021-05-12 20:00" : ["Pelicans","Home"],
                         "2021-05-14 20:00" : ["Raptors","Home"],
                         "2021-05-16 19:30" : ["Timberwolves","Home"]}


mavs_games = []

def compile_game_info(games_array):
    for g_date_time, g_opp_location in games_array.items():
        date_times = g_date_time.split(" ")
        for date_list in date_times:
            print(date_list)
            print(type(date_list))
            g_date = date_list[0]
            g_time = date_list[1]

            #print(g_date)
            #print(g_time)


        #game = SportsEvent()

compile_game_info(mavs_game_dates_times)













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
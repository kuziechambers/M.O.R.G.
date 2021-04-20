import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as panda

def percent_to_float(x):
    return float(x.strip('%'))/100

url = "https://www.basketball-reference.com/teams/DAL/2021_games.html"

#try:
driver = webdriver.Chrome("/Users/kuziechambers/chromedriver")
driver.set_window_size(200, 1000)
driver.get(url)
driver.implicitly_wait(5)


table_div = driver.find_element_by_id("games")
table_body = table_div.find_element_by_tag_name("tbody")
table_rows = table_body.find_elements_by_tag_name("tr")

player_names = []
teams_list = []
freqs_list = []

for row in table_rows:
    print(row)
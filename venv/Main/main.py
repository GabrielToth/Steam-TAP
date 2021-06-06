import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=any&appid=730"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

driver.quit()
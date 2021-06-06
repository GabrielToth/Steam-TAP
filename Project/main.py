import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B0%5D=any&category_730_ProPlayer%5B0%5D=any&category_730_StickerCapsule%5B0%5D=any&category_730_TournamentTeam%5B0%5D=any&category_730_Weapon%5B0%5D=any&appid=730"

option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath('//div[@id="mainContents"]//div[@id="sideBar"]//div[@id="findItems"]//div[@class="market_search_sidebar_contents"]//div[@class="market_search_box_container"]//form[@id="market_search"]//div[@class="market_search_input_container"]//div[@id="market_search_advanced_show"]//div[@class="market_search_advanced_button"]').click()
# Pra selecionar o valor da skin//div[@id='searchResultsRows']//div[@class='market_listing_row_link']//div[@class='market_listing_row market_recent_listing_row market_listing_searchresult']//div[@class='market_listing_price_listings_block']//div[@class='market_listing_right_cell market_listing_their_price']//span[@class='market_table_value normal_price']//span[@class='normal_price']
driver.find_element_by_xpath('//div[@id="market_advancedsearch_filters"]//div[@class="econ_tag_filter_category"]//div[@class="econ_tag_filter_container"]//input[@id="tag_730_Exterior_WearCategory0"]').click()
driver.find_element_by_xpath('//div[@id="market_advancedsearch_filters"]//div[@class="econ_tag_filter_category"]//div[@class="econ_tag_filter_container"]//input[@id="tag_730_Quality_normal"]').click()
driver.find_element_by_xpath('//div[@id="market_advancedsearch_filters"]//div[@class="econ_tag_filter_category"]//div[@class="econ_tag_filter_container"]//input[@id="tag_730_Rarity_Rarity_Common_Weapon"]').click()
driver.find_element_by_xpath('//div[@id="market_advancedsearch_filters"]//div[@class="econ_tag_filter_category"]//div[@class="econ_tag_filter_container"]//input[@id="tag_730_Type_CSGO_Type_Pistol"]').click()
driver.find_element_by_xpath('//div[@class="market_advancedsearch_bottombuttons"]//div[@class="btn_medium btn_green_white_innerfade"]').click()
time.sleep(10)

driver.quit()


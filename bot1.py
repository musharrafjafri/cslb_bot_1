from csv import reader
import time
import requests
import pandas as pd
from time import sleep
from selenium import webdriver
from _collections import defaultdict
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#

input_data = []
with open('input_data/input_data.csv', 'r') as data:
    # pass the file object to reader() to get the reader object
    read_data = reader(data)
    # Iterate over each row in the csv using reader object
    for row in read_data:
        # row variable is a list that represents a row in csv
        input_data.append(row)


for num in range(len(input_data)):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('start-maximized')
    preferances = {"download.default_directory": r"C:\Users\smmj1\OneDrive\Python Projects\cslb_bot-1\output_data"}
    options.add_experimental_option("prefs", preferances)
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://cslb.ca.gov/OnlineServices/CheckLicenseII/ZipCodeSearch.aspx")
    sleep(1)

    poped_row = input_data.pop()
    city = poped_row[0]
    lic_type = poped_row[1]

    driver.find_element_by_name('ctl00$MainContent$txtCity').send_keys(city)
    selection = Select(driver.find_element_by_name('ctl00$MainContent$ddlLicenseType'))
    selection.select_by_visible_text(lic_type)
    driver.find_element_by_name('ctl00$MainContent$btnZipCodeSearch').click()
    sleep(2)
    driver.find_element_by_name('ctl00$MainContent$ibExportToExcell').click()
    sleep(10)
    driver.close()

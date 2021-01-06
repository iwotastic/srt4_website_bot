from selenium import webdriver
from selenium.webdriver.common.by import By
from console import console
from bot_session import SequentialBotSession
import json

# General config

index_url = "https://127.0.0.1:5000"
with open("form_index.json") as form_index:
  forms = json.load(form_index)

# Start up the Safari webdriver...

browser = webdriver.Safari()

sbs = SequentialBotSession(browser)
sbs.execute(index_url + "/" + forms[0])
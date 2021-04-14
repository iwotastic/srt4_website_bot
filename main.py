from selenium import webdriver
from selenium.webdriver.common.by import By
from console import console
from rich.progress import track
import bot_session
import json
console.print("[grey50]Getting ready...[/]")

# General config

num_randoms_per_page = 2 # Number of random submissions per page per browser
index_url = "http://127.0.0.1:5000" # Base URL
with open("form_index.json") as form_index: # Load form index
  forms = json.load(form_index)

# Set up browser routines...

def execute_bot_data_routine(browser, name):
  routines = []
  routines += [(bot_session.SequentialBotSession, form) for form in forms]
  routines += [(bot_session.RandomBotSession, form) for form in forms for _ in range(num_randoms_per_page)]
  routines += [(bot_session.StraightLineBotSession, form) for form in forms for _ in range(num_randoms_per_page)]
  routines += [(bot_session.ExponentialBotSession, form) for form in forms for _ in range(num_randoms_per_page)]
  routines += [(bot_session.SinBotSession, form) for form in forms for _ in range(num_randoms_per_page)]
  routines += [(bot_session.WiggleLineBotSession, form) for form in forms for _ in range(num_randoms_per_page)]
  
  for bsc, form in track(routines, f"Using [b green4]{name}[/]"):
    bs = bsc(browser)
    bs.execute(index_url + "/" + form)

  browser.quit()

console.print("[bold green]Ready![/]")

# Execute routines...

safari = webdriver.Safari()
execute_bot_data_routine(safari, "Safari")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(options=chrome_options)
execute_bot_data_routine(chrome, "Chrome")

console.rule("Complete!")
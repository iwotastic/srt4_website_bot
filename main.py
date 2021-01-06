from selenium import webdriver
from selenium.webdriver.common.by import By
from console import console
from rich.progress import track
from bot_session import RandomBotSession
import json
console.print("[grey50]Getting ready...[/]")

# General config

num_randoms_per_page = 20 # Number of random submissions per page per browser
index_url = "http://127.0.0.1:5000" # Base URL
with open("form_index.json") as form_index: # Load form index
  forms = json.load(form_index)

# Set up browser routines...

def execute_bot_data_routine(browser):
  sbs = RandomBotSession(browser)
  for form in forms:
    for _ in track(range(num_randoms_per_page), f"Submitting [b blue]{form}[/]..."):
      sbs.execute(index_url + "/" + form)

  browser.quit()

# Execute routines...

console.print("[bold green]Ready![/]")
console.rule("Google Chrome")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome(options=chrome_options)
execute_bot_data_routine(chrome)

console.rule("Safari")
safari = webdriver.Safari()
execute_bot_data_routine(safari)

console.rule("Complete!")
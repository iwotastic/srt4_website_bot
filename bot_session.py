from selenium.webdriver.common.by import By
from console import console
from utils import rand_email, rand_text

class SequentialBotSession:
  def __init__(self, browser):
    self.browser = browser

  def order(self, elements):
    pass

  def handle_input_type_text(self, el):
    el.click()
    el.send_keys(rand_text(10, 20))

  def handle_input_type_email(self, el):
    el.click()
    el.send_keys(rand_email())

  def handle_textarea(self, el):
    el.click()
    el.send_keys(rand_text(70, 110))

  def execute(self, url):
    self.browser.get(url)

    input_elements = self.browser.find_elements(By.TAG_NAME, "input")
    select_elements = self.browser.find_elements(By.TAG_NAME, "select")
    textarea_elements = self.browser.find_elements(By.TAG_NAME, "textarea")

    elements = input_elements + select_elements + textarea_elements
    self.order(elements)

    for el in elements:
      tag_name = el.tag_name.lower()
      if tag_name == "input":
        getattr(self, f"handle_input_type_{el.get_attribute('type')}", lambda _: None)(el)
      else:
        getattr(self, f"handle_{tag_name}", lambda _: None)(el)

    
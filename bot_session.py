from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils import rand_email, rand_text, move_mouse_based_on_func
from random import random, randrange, shuffle, uniform
from rich.progress import track
import time

class SequentialBotSession:
  def __init__(self, browser):
    self.browser = browser
    self.password = ""

  def order(self, elements):
    pass

  def handle_input_type_text(self, el):
    el.click()
    el.send_keys(rand_text(10, 20))

  def handle_input_type_email(self, el):
    el.click()
    el.send_keys(rand_email())

  def handle_input_type_password(self, el):
    el.click()
    el.send_keys(self.password)

  def handle_textarea(self, el):
    el.click()
    el.send_keys(rand_text(70, 110))

  def execute(self, url):
    self.browser.get(url)
    self.password = rand_text(10, 20)

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

    self.browser.find_element_by_css_selector("button[type=submit]").click()
    time.sleep(0.2)

class RandomBotSession(SequentialBotSession):
  def order(self, elements):
    shuffle(elements)

class StraightLineBotSession(SequentialBotSession):
  def __init__(self, browser):
    SequentialBotSession.__init__(self, browser)
    self.last_x = 0
    self.last_y = 0

  def execute(self, url):
    # Set mouse position to top middle of viewport (or somewhere around there)
    self.last_x = int((0.25 + 0.5 * random()) * self.browser.get_window_size()["width"])
    self.last_y = 0

    ac = ActionChains(self.browser)
    ac.w3c_actions.pointer_action.move_to_location(self.last_x, self.last_y)
    ac.perform()

    SequentialBotSession.execute(self, url)

  def click_element(self, el):
    x_to_click = el.rect["x"] + 5 + randrange(el.rect["width"] - 10)
    y_to_click = el.rect["y"] + 5 + randrange(el.rect["height"] - 10)
    move_mouse_based_on_func(
      self.browser,
      (self.last_x, self.last_y),
      (x_to_click, y_to_click),
      lambda x: x,
      [uniform(0, 0.02) for _ in range(randrange(2, 5))]
    )

    ActionChains(self.browser).click().perform()

  def handle_input_type_text(self, el):
    self.click_element(el)
    el.send_keys(rand_text(10, 20))

  def handle_input_type_email(self, el):
    self.click_element(el)
    el.send_keys(rand_email())

  def handle_input_type_password(self, el):
    self.click_element(el)
    el.send_keys(self.password)

  def handle_textarea(self, el):
    self.click_element(el)
    el.send_keys(rand_text(70, 110))

class ExponentialBotSession(StraightLineBotSession):
  def click_element(self, el):
    x_to_click = el.rect["x"] + 5 + randrange(el.rect["width"] - 10)
    y_to_click = el.rect["y"] + 5 + randrange(el.rect["height"] - 10)
    exp = uniform(0.01, 3)
    move_mouse_based_on_func(
      self.browser,
      (self.last_x, self.last_y),
      (x_to_click, y_to_click),
      lambda x: x ** exp,
      [uniform(0, 0.02) for _ in range(randrange(2, 5))]
    )

    ActionChains(self.browser).click().perform()
import random
from selenium.webdriver import ActionChains
import time

_text_characters = "".join([chr(c) for c in range(ord("a"), ord("z"))])
_text_characters += "".join([chr(c) for c in range(ord("A"), ord("Z"))])
_text_characters += "".join([chr(c) for c in range(ord("0"), ord("9"))])

def rand_text(min_length, max_length, spaces=True):
  result = ""
  rand_chars = _text_characters + (" " if spaces else "")

  for _ in range(random.randint(min_length, max_length)):
    result += random.choice(rand_chars)

  return result

def rand_email():
  return rand_text(5, 20, spaces=False) + "@" + rand_text(3, 12, spaces=False) + ".com"

def move_mouse_based_on_func(browser, origin, dest, func, timing):
  ac = ActionChains(browser)

  # Teleport mouse to orgin
  ac.w3c_actions.pointer_action.move_to_location(origin[0], origin[1])
  ac.perform()

  # Generate XY values for func based on timing
  func_xs = [(x + 1) / len(timing) for x in range(len(timing))]
  func_ys = [func(y) for y in func_xs]

  for func_x, func_y, delay in zip(func_xs, func_ys, timing):
    # Perform delay specified by timimg iterable
    time.sleep(abs(delay))

    # Move mouse to specified point
    ac.w3c_actions.pointer_action.move_to_location(
      func_x * (dest[0] - origin[0]) + origin[0],
      func_y * (dest[1] - origin[1]) + origin[1]
    )
    ac.perform()

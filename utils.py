import random

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
  return rand_text(5, 20) + "@" + rand_text(3, 12) + ".com"
from selenium import webdriver

index_url = "https://srt4project.ianmorrill.com"

browser = webdriver.Safari()
browser.get(index_url)
links = browser.find_elements_by_tag_name("a")

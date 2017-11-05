from func.get_data import *
import selenium

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- FUTURISM SCRAPE-- #
try:
    try:
        chrome.get("https://futurism.com/?s=basic+income")
    except selenium.common.exceptions.TimeoutException:
        try:
            chrome.get("https://futurism.com/?s=basic+income")
        except selenium.common.exceptions.TimeoutException:
            chrome.get("https://futurism.com/?s=basic+income")

    data467657o = chrome.find_elements_by_class_name("title")
    for each98758 in data467657o:
        links += [each98758.get_attribute("href")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("futurism", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "futurism")
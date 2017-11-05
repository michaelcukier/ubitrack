from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- PRECARIOUS WORK SCRAPE-- #
try:
    chrome.get("http://www.precariouswork.com/?s=basic+income")

    data46788657o98 = chrome.find_elements_by_css_selector("article h2 a")

    precariousLINKS = []
    for every55336 in data46788657o98:
        links += [every55336.get_attribute("href")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("precarious work", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "precarious work")
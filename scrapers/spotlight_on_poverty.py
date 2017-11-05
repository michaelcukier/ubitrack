from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- SPOTLIGHT ON POVERTY SCRAPE-- #
try:
    chrome.get("https://spotlightonpoverty.org/?s=basic+income")

    findLinksSPOTLIGHT = chrome.find_elements_by_css_selector("article div.entry h3 a")

    for every5666yu in findLinksSPOTLIGHT:
        links += [every5666yu.get_attribute("href")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("spotlight on poverty", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "spotlight on poverty")
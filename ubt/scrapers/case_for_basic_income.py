from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- GOOGLE NEWS SCRAPE-- #
try:

    chrome.get("http://www.caseforbasicincome.com/category/basic-income-news/")
    caseForBI = chrome.find_elements_by_css_selector("h2.entry-title a")
    for all8677777 in caseForBI:
        links += [all8677777.get_attribute("href")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("case for basic income", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "case for basic income")
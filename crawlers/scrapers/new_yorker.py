from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- NEW YORKER SCRAPE --
try:
    chrome.get("http://www.newyorker.com/search?q=basic+income")

    linksFromNY = []
    try:
        linksFromNY = chrome.find_elements_by_css_selector("h2.title a")
    except selenium.common.exceptions.TimeoutException:
        linksFromNY = chrome.find_elements_by_css_selector("h2.title a")

    allTitlesNY = []
    allLinksNY = []

    for every67hyjuki99 in linksFromNY:
        try:
            allLinksNY += [every67hyjuki99.get_attribute("href")]
            allTitlesNY += [every67hyjuki99.text]
        except selenium.common.exceptions.TimeoutException:
            allLinksNY += [every67hyjuki99.get_attribute("href")]
            allTitlesNY += [every67hyjuki99.text]

    for ikergegf67599jjj in range (0, len(allLinksNY)):
        if ("basic income" in allTitlesNY[ikergegf67599jjj]) or ("Basic income" in allTitlesNY[ikergegf67599jjj]) or ("UBI" in allTitlesNY[ikergegf67599jjj]) or ("Basic Income" in allTitlesNY[ikergegf67599jjj]) or ("Guaranteed Income" in allTitlesNY[ikergegf67599jjj]):
            links += [allLinksNY[ikergegf67599jjj]]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("new yotker", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "new yorker")
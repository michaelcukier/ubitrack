from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- BBC SCRAPE-- #
try:
    chrome.get("http://www.bbc.co.uk/search?q=basic+income&filter=news")

    findAllTitlesBBC = chrome.find_elements_by_css_selector("div h1 a")

    allTitlesBBC = []
    allLinksBBC = []

    for eachBBC in findAllTitlesBBC:
        allTitlesBBC.append(eachBBC.text)
        allLinksBBC.append(eachBBC.get_attribute("href"))

    interestingIndexBBC = []
    for eachBBC2 in allTitlesBBC:
        if ("Basic Income" in eachBBC2) or ("Basic income" in eachBBC2) or ("UBI" in eachBBC2) or ("basic income" in eachBBC2):
            interestingIndexBBC.append(allTitlesBBC.index(eachBBC2))

    for indexBBC in interestingIndexBBC:
        links.append(allLinksBBC[indexBBC])

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("bbc", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "bbc")
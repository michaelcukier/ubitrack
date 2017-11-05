from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- L.A. Times SCRAPE-- #
try:

    try:
        chrome.get("http://www.latimes.com/search/dispatcher.front?target=stories&spell=on&Query=basic%20income&sortby=display_time%20descending#trb_search")
    except selenium.common.exceptions.TimeoutException:
        try:
            chrome.get("http://www.latimes.com/search/dispatcher.front?target=stories&spell=on&Query=basic%20income&sortby=display_time%20descending#trb_search")
        except selenium.common.exceptions.TimeoutException:
            chrome.quit()
            display.stop()
            quit()

    findAllLATIMESTitlesAndLinks = chrome.find_elements_by_css_selector("a.trb_search_result_title")
    findAllLATIMESBriefs = chrome.find_elements_by_css_selector("div.trb_search_result_description")

    allTitlesLA = []
    allLinksLA = []
    allBriefsLA = []
    for eachLA in findAllLATIMESTitlesAndLinks:
        allTitlesLA.append(eachLA.text)
        allLinksLA.append(eachLA.get_attribute("href"))

    for eachLA1 in findAllLATIMESBriefs:
        allBriefsLA.append(eachLA1.text)

    interestingIndexesLA = []
    for everyLA1 in allTitlesLA:
        if ("basic income" in everyLA1) or ("Basic income" in everyLA1) or ("Basic Income" in everyLA1) or ("UBI" in everyLA1):
            if allTitlesLA.index(everyLA1) not in interestingIndexesLA:
                interestingIndexesLA.append(allTitlesLA.index(everyLA1))

    for everyLA2 in allBriefsLA:
        if ("basic income" in everyLA2) or ("Basic income" in everyLA2) or ("Basic Income" in everyLA2) or ("UBI" in everyLA2):
            if allBriefsLA.index(everyLA2) not in interestingIndexesLA:
                interestingIndexesLA.append(allBriefsLA.index(everyLA2))

    for indexLA in interestingIndexesLA:
        links.append(allLinksLA[indexLA])


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("l.a. times", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "la times")
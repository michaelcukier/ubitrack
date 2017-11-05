from func.get_data import *
import selenium
import time

# -- WEBDRIVER -- #
chrome, display = load_chrome()


# -- TECH CRUNCH SCRAPE-- #
links = []

try:
    accessUrl("https://techcrunch.com/search/basic+income#stq=basic income&stp=1", "techcrunch")

    try:
        buttonClick86467 = chrome.find_element_by_xpath('//*[@id="recent-sort-selector"]')
    except selenium.common.exceptions.NoSuchElementException:
        time.sleep(5)
        chrome.get("https://techcrunch.com/search/basic+income#stq=basic income&stp=1")
        buttonClick86467 = chrome.find_element_by_xpath('//*[@id="recent-sort-selector"]')

    buttonClick86467.click()
    time.sleep(5)

    linkOfTechCrunch = []
    briefTC10 = []
    briefTC100 = []

    for fatboss2 in range(1, 100):
        try:
            allLinksTECH = chrome.find_element_by_xpath('//*[@id="st-results-container"]/li[' + str(fatboss2) + ']/div/div/h2/a')
            linkOfTechCrunch += [allLinksTECH.get_attribute("href")]
            allLinksBriefTC = chrome.find_element_by_xpath('//*[@id="st-results-container"]/li[' + str(fatboss2) + ']/div/div/p')
            briefTC10 += [allLinksBriefTC.text]
            briefTC100 += [allLinksTECH.text]
        except selenium.common.exceptions.NoSuchElementException:
            pass

    ikaList = []
    for ika in briefTC10:
        if ("basic income" in ika) or ("Basic income" in ika) or ("Basic Income" in ika) or ("UBI" in ika):
            ikaList += [briefTC10.index(ika)]

    ika2List = []
    for ika2 in briefTC100:
        if ("basic income" in ika2) or ("Basic income" in ika2) or ("Basic Income" in ika2) or ("UBI" in ika2):
            ika2List += [briefTC100.index(ika2)]

    brandNewList = ikaList + ika2List

    cleanListOfINDEX = []
    for i99 in brandNewList:
        if i99 not in cleanListOfINDEX:
            cleanListOfINDEX.append(i99)

    for interestingLinksOnly99 in cleanListOfINDEX:
        links += [linkOfTechCrunch[interestingLinksOnly99]]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("tech crunch", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "techcrunch")
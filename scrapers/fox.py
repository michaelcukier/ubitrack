from func.get_data import *
import selenium

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- FOX SCRAPE-- #
try:
    chrome.get("http://www.foxnews.com/search-results/search?q=basic%20income&ss=fn&sort=latest&start=0")

    findAllTitlesAndLinksFOXNEWS = []
    for iteraFOX in range(3, 14):
        try:
            findAllTitlesAndLinksFOXNEWS.append(chrome.find_element_by_xpath('//*[@id="search-container"]/div[' + str(iteraFOX) + ']/div/div/h3/a'))
        except selenium.common.exceptions.NoSuchElementException:
            pass

    allTitlesFOX = []
    allLinksFOX = []
    for elemFOX in findAllTitlesAndLinksFOXNEWS:
        allLinksFOX.append(elemFOX.get_attribute("href"))
        allTitlesFOX.append(elemFOX.text)

    findAllBriefsFOX = chrome.find_elements_by_css_selector("p.ng-binding.ng-scope")
    allBriefsFox = []
    for elemFOX2 in findAllBriefsFOX:
        allBriefsFox.append(elemFOX2.text)

    interestingIndexesFOX = []
    for everyFox in allTitlesFOX:
        if ("basic income" in everyFox) or ("Basic income" in everyFox) or ("Basic Income" in everyFox) or ("UBI" in everyFox):
            if allTitlesFOX.index(everyFox) not in interestingIndexesFOX:
                interestingIndexesFOX.append(allTitlesFOX.index(everyFox))

    for everyFox1 in allBriefsFox:
        if ("basic income" in everyFox1) or ("Basic income" in everyFox1) or ("Basic Income" in everyFox1) or ("UBI" in everyFox1):
            if allBriefsFox.index(everyFox1) not in interestingIndexesFOX:
                interestingIndexesFOX.append(allBriefsFox.index(everyFox1))

    for indexFox99 in interestingIndexesFOX:
        links.append(allLinksFOX[indexFox99])


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("fox", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "fox")
from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- GOOGLE NEWS SCRAPE-- #
try:
    chrome.get("https://qz.com/search/basicincome")

    findAllTitlesAndLinksQZ = chrome.find_elements_by_css_selector("h2.queue-article-title a")
    findAllBriefsQZ = chrome.find_elements_by_css_selector("p.queue-article-summary")

    allTitlesQZ = []
    allLinksQZ = []
    allBriefsQZ = []
    for eachQZ in findAllTitlesAndLinksQZ:
        allTitlesQZ.append(eachQZ.text)
        allLinksQZ.append(eachQZ.get_attribute("href"))

    for eachQZ1 in findAllBriefsQZ:
        allBriefsQZ.append(eachQZ1.text)

    interestingIndexesQZ = []
    for everyQZ1 in allTitlesQZ:
        if ("basic income" in everyQZ1) or ("Basic income" in everyQZ1) or ("Basic Income" in everyQZ1) or ("UBI" in everyQZ1):
            if allTitlesQZ.index(everyQZ1) not in interestingIndexesQZ:
                interestingIndexesQZ.append(allTitlesQZ.index(everyQZ1))

    for everyQZ2 in allBriefsQZ:
        if ("basic income" in everyQZ2) or ("Basic income" in everyQZ2) or ("Basic Income" in everyQZ2) or ("UBI" in everyQZ2):
            if allBriefsQZ.index(everyQZ2) not in interestingIndexesQZ:
                interestingIndexesQZ.append(allBriefsQZ.index(everyQZ2))

    for indexQZ in interestingIndexesQZ:
        links.append(allLinksQZ[indexQZ])


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("quartz", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "quartz")
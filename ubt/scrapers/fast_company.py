from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- GOOGLE NEWS SCRAPE-- #
try:
    accessUrl("https://www.fastcompany.com/search/basic%20income", "fast company")

    findAllTitlesFastC = chrome.find_elements_by_css_selector("h2.title.all-feed__title")
    findAllBriefsFastC = chrome.find_elements_by_css_selector("h3.deck.all-feed__deck")
    findAllLinksFastC = chrome.find_elements_by_css_selector("article.card.all-feed__card a")

    allTitlesFastC = []
    allLinksFastC = []
    allBriefsFastC = []

    for FC1 in findAllTitlesFastC:
        allTitlesFastC.append(FC1.text)
    for FC2 in findAllBriefsFastC:
        allBriefsFastC.append(FC2.text)
    for FC3 in findAllLinksFastC:
        allLinksFastC.append(FC3.get_attribute("href"))

    interestingIndexesFastC = []
    for everyFC1 in allTitlesFastC:
        if ("basic income" in everyFC1) or ("Basic income" in everyFC1) or ("Basic Income" in everyFC1) or ("UBI" in everyFC1):
            if allTitlesFastC.index(everyFC1) not in interestingIndexesFastC:
                interestingIndexesFastC.append(allTitlesFastC.index(everyFC1))

    for everyFC2 in allBriefsFastC:
        if ("basic income" in everyFC2) or ("Basic income" in everyFC2) or ("Basic Income" in everyFC2) or ("UBI" in everyFC2):
            if allBriefsFastC.index(everyFC2) not in interestingIndexesFastC:
                interestingIndexesFastC.append(allBriefsFastC.index(everyFC2))

    for indexFox99 in interestingIndexesFastC:
        links.append(allLinksFastC[indexFox99])


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("fast company", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "fast company")
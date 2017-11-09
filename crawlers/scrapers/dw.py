from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- DW SCRAPE-- #
try:
    accessUrl("http://www.dw.com/search/?languageCode=en&item=basic%20income&sort=DATE&resultsCounter=10", "dw")

    getAllTitlesDW = chrome.find_elements_by_css_selector("div.tw h2")
    getAllLinksDW = chrome.find_elements_by_css_selector("div.searchResult a")
    getAllBriefsDW = chrome.find_elements_by_css_selector("div.searchResult a div.tw p")

    titlesDW = []
    linksBW = []
    briefsDW = []

    for ikoDW in range(0, len(getAllTitlesDW)):
        titlesDW.append(getAllTitlesDW[ikoDW].text)
        linksBW.append(getAllLinksDW[ikoDW].get_attribute("href"))
        briefsDW.append(getAllBriefsDW[ikoDW].text)

    interestingIndexesDW = []
    for everyDW1 in titlesDW:
        if ("basic income" in everyDW1) or ("Basic income" in everyDW1) or ("Basic Income" in everyDW1) or ("UBI" in everyDW1):
            if titlesDW.index(everyDW1) not in interestingIndexesDW:
                interestingIndexesDW.append(titlesDW.index(everyDW1))

    for everyDW2 in briefsDW:
        if ("basic income" in everyDW2) or ("Basic income" in everyDW2) or ("Basic Income" in everyDW2) or ("UBI" in everyDW2):
            if briefsDW.index(everyDW2) not in interestingIndexesDW:
                interestingIndexesDW.append(briefsDW.index(everyDW2))

    for indexDW in interestingIndexesDW:
        links.append(linksBW[indexDW])


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("dw", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "dw")
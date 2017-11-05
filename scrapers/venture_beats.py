from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- VENTURE BEAT SCRAPE-- #
try:
    chrome.get("https://venturebeat.com/?s=basic%20income")

    getVBtitleListAndLinks = chrome.find_elements_by_css_selector("h2.article-title a")

    VBtitleList = []
    VBLinkList = []

    for eachVB in getVBtitleListAndLinks:
        VBtitleList.append(eachVB.text)
        VBLinkList.append(eachVB.get_attribute("href"))

    interestingIndexesVB = []
    for eachTitleVB in VBtitleList:
        if ("Basic Income" in eachTitleVB) or ("Basic income" in eachTitleVB) or ("UBI" in eachTitleVB) or ("basic income" in eachTitleVB):
            interestingIndexesVB.append(VBtitleList.index(eachTitleVB))

    for eachIndexVB in interestingIndexesVB:
        links.append(VBLinkList[eachIndexVB])

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("venture beats", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "venture beats")
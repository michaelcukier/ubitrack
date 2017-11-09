from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- THE INDEPENDENT SCRAPE-- #
try:
    try:
        chrome.get("http://www.independent.co.uk/search/site/basic%2520income")
        getINDEPENDENT = chrome.find_elements_by_css_selector("div.body h2 a")
        getIndependt2 = chrome.find_elements_by_class_name("search-snippet")
    except selenium.common.exceptions.TimeoutException:
        chrome.get("http://www.independent.co.uk/search/site/basic%2520income")
        getINDEPENDENT = chrome.find_elements_by_css_selector("div.body h2 a")
        getIndependt2 = chrome.find_elements_by_class_name("search-snippet")

    INDEtitleList = []
    INDElinksList = []
    INDEbriefList = []

    for each8896zz in getINDEPENDENT:
        INDEtitleList += [each8896zz.text]
        INDElinksList += [each8896zz.get_attribute("href")]

    for each88807hhh67 in getIndependt2:
        INDEbriefList += [each88807hhh67.text]

    interestedINDETITLES = []
    interestedINDEBRIEFS = []

    for ikzd8897hhhef6 in range(0, len(INDEbriefList)):

        if ("Basic Income" in INDEtitleList[ikzd8897hhhef6]) or ("Basic income" in INDEtitleList[ikzd8897hhhef6]) or ("UBI" in INDEtitleList[ikzd8897hhhef6]) or ("basic income" in INDEtitleList[ikzd8897hhhef6]):
            interestedINDETITLES += [INDEtitleList[ikzd8897hhhef6]]

        if ("Basic Income" in INDEbriefList[ikzd8897hhhef6]) or ("Basic income" in INDEbriefList[ikzd8897hhhef6]) or ("UBI" in INDEbriefList[ikzd8897hhhef6]) or ("basic income" in INDEbriefList[ikzd8897hhhef6]):
            interestedINDEBRIEFS += [INDEbriefList[ikzd8897hhhef6]]

    interestingIndexes9990111koil = []

    for each1686hh in interestedINDETITLES:
        interestingIndexes9990111koil += [interestedINDETITLES.index(each1686hh)]

    for eacxxh77972 in interestedINDEBRIEFS:
        interestingIndexes9990111koil += [interestedINDEBRIEFS.index(eacxxh77972)]

    interestingIndexes9990111koilClean = []

    for everyIndexin987 in interestingIndexes9990111koil:
        if everyIndexin987 not in interestingIndexes9990111koilClean:
            interestingIndexes9990111koilClean += [everyIndexin987]

    for clean7765YEAH in interestingIndexes9990111koilClean:
        links += [INDElinksList[clean7765YEAH]]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("the independent", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "the independent")
from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- NEW YORK TIMES SCRAPE-- #
try:
    chrome.get("https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/basic+income/since1851/document_type%3A%22article%22/1/allauthors/newest/")

    allTitlesNYTIMES = []
    allBriefsNYTIMES = []
    allLinksNYTIMES = []

    findNYTIMES = chrome.find_elements_by_css_selector("div.element2 h3 a")
    findNYTIMESBRIEFS = chrome.find_elements_by_class_name("summary")

    for eachNYTIMES in findNYTIMES:
        allTitlesNYTIMES.append(eachNYTIMES.text)
        allLinksNYTIMES.append(eachNYTIMES.get_attribute("href"))

    for elem08796HH in findNYTIMESBRIEFS:
        allBriefsNYTIMES.append(elem08796HH.text)

    for i57699NYT in range(0, len(allTitlesNYTIMES)):
        if ("basic income" in allTitlesNYTIMES[i57699NYT]) or ("UBI" in allTitlesNYTIMES[i57699NYT]) or ("Basic Income" in allTitlesNYTIMES[i57699NYT]) or ("Basic income" in allTitlesNYTIMES[i57699NYT]):
            links += [allLinksNYTIMES[i57699NYT]]

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("ny times", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "ny times")
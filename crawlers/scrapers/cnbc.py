from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- cnbc SCRAPE-- #
try:
    chrome.get("http://search.cnbc.com/rs/search/view.html?partnerId=2000&keywords=basic%20income&sort=date&type=news&source=CNBC.com,The%20Reformed%20Broker,Buzzfeed,Estimize,Curbed,Polygon,Racked,Eater,SB%20Nation,Vox,The%20Verge,Recode,Breakingviews,NBC%20News,The%20Today%20Show,Fiscal%20Times,The%20New%20York%20Times,Financial%20Times,USA%20Today&assettype=partnerstory,blogpost,wirestory,cnbcnewsstory&pubtime=30&pubfreq=d")
    linksFromCNBC = chrome.find_elements_by_css_selector("h3.title a")
    for every67hyjuki in linksFromCNBC:
        links += [every67hyjuki.get_attribute("href")]

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("cnbc", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "cnbc")
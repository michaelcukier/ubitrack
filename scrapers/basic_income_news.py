from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []


# -- GOOGLE NEWS SCRAPE-- #
try:
    chrome.get("http://basicincome.org/news/category/news-events/")
    allTheABranch = chrome.find_elements_by_css_selector('h2.post-title a')
    for linkOfBI in allTheABranch:
        if "basicincome.org/topic/" not in linkOfBI.get_attribute('href'):
            theLink = linkOfBI.get_attribute('href')
            links += [theLink]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("basic income news", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "basic income news")
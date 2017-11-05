from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- GOOGLE NEWS SCRAPE-- #
try:
    chrome.get('https://news.google.com/news/search/section/q/basic%20income/basic%20income?hl=en-GB&ned=uk')

    findAllLinksGN = chrome.find_elements_by_css_selector('a.nuEeue')

    for lk in findAllLinksGN:
        if lk.text != "":
            if "stocknewsgazette" not in lk.get_attribute("href"):
                if "argusjournal" not in lk.get_attribute("href"):
                    links.append(lk.get_attribute("href").replace("https", "http"))


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("google news", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "google news")
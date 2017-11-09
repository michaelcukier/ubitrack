from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()


# -- REDDIT SCRAPE-- #
links = []

try:
    try:
        chrome.get("https://www.reddit.com/r/BasicIncome/new/")
    except selenium.common.exceptions.TimeoutException:
        try:
            chrome.get("https://www.reddit.com/r/BasicIncome/new/")
        except selenium.common.exceptions.TimeoutException:
            chrome.get("https://www.reddit.com/r/BasicIncome/new/")

    getAllLinksREDDIT = chrome.find_elements_by_css_selector("p.title a")

    allDirtyRedditLinks = []
    for eachRedditLink in getAllLinksREDDIT:
        if (eachRedditLink.get_attribute("data-href-url") != None) and ("/r/BasicIncome/comments/" not in eachRedditLink.get_attribute("data-href-url")):
            allDirtyRedditLinks += [eachRedditLink.get_attribute("data-href-url")]

    for linkREDDIT99 in allDirtyRedditLinks:
        if "reddit" not in linkREDDIT99:
            if "i.redd.it" not in linkREDDIT99:
                if "facebook.com" not in linkREDDIT99:
                    if "medium.com" not in linkREDDIT99:
                        if "youtube.com" not in linkREDDIT99:
                            if "facebook.com" not in linkREDDIT99:
                                if "wikipedia.org" not in linkREDDIT99:
                                    if "imgur.com" not in linkREDDIT99:
                                        if "youtu.be" not in linkREDDIT99:
                                            if "linkedin.com" not in linkREDDIT99:
                                                if "ft.com" not in linkREDDIT99:
                                                    if "twitter.com" not in linkREDDIT99:
                                                        if "docs.google.com" not in linkREDDIT99:
                                                            if "drive.google.com" not in linkREDDIT99:
                                                                if ".fm" not in linkREDDIT99:
                                                                    if "vimeo.com" not in linkREDDIT99:
                                                                        if ".wordpress.com" not in linkREDDIT99:
                                                                            if "patreon.com" not in linkREDDIT99:
                                                                                if "basicincome.org/topic/" not in linkREDDIT99:
                                                                                    if "podcast" not in linkREDDIT99:
                                                                                        if "forbes.com" not in linkREDDIT99:
                                                                                            if "businessinsider" not in linkREDDIT99:
                                                                                                if "google.com/trends/explore" not in linkREDDIT99:
                                                                                                    if "trends.google.com/trends/explore" not in linkREDDIT99:
                                                                                                        if "wiki" not in linkREDDIT99:
                                                                                                            if "amazon." not in linkREDDIT99:
                                                                                                                if ".blogspot." not in linkREDDIT99:
                                                                                                                    if "putlocker" not in linkREDDIT99:
                                                                                                                        links += [linkREDDIT99.replace("https", "http")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("reddit", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "reddit")
from func.get_data import *
import selenium

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- WASHINGTON POST SCRAPE-- #
try:
    accessUrl('https://www.washingtonpost.com/newssearch/?datefilter=All%20Since%202005&query=basic%20income&sort=Date&utm_term=.5f52c11310e7', 'the washington post')
    listOfAllTitles12 = []
    listOfAllBriefings12 = []
    for itera in range(1, 30):
        try:
            find_all_titles = chrome.find_element_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/div[' + str(itera) + ']/div[1]/p/a')
            data = find_all_titles.get_attribute("data-ng-href")
            listOfAllTitles12 += [data]
            find_all_briefing = chrome.find_element_by_xpath('//*[@id="main-content"]/div/div/div[2]/div/div[' + str(itera) + ']/div[2]')
            data2 = find_all_briefing.text
            listOfAllBriefings12 += [data2]
        except selenium.common.exceptions.NoSuchElementException:
            pass

    for every323 in range(0, len(listOfAllTitles12)):
        if ("basic income" in listOfAllBriefings12[every323]) or ("UBI" in listOfAllBriefings12[every323]) or ("Basic income" in listOfAllBriefings12[every323]) or ("Basic Income" in listOfAllBriefings12[every323]):
            links += [listOfAllTitles12[every323]]

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("washington post", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "washington post")
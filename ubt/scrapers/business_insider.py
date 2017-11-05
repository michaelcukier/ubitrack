from func.get_data import *
import selenium

# -- WEBDRIVER -- #
chrome, display = load_chrome()


# -- BUSINESS INSIDER SCRAPE-- #
links = []

try:
    chrome.get("http://www.businessinsider.com/s?q=basic+income&vertical=&author=&contributed=1&sort=date")

    buttonClick86467 = chrome.find_elements_by_class_name("excerpt")
    listOfRAEA = []

    for zevae in buttonClick86467:
        if ("Basic Income" in zevae.text) or ("Basic income" in zevae.text)  or ("basic income" in zevae.text) or ("UBI" in zevae.text):
            getIndex9876 = buttonClick86467.index(zevae)
            listOfRAEA += [getIndex9876]

    listKioooo = []
    for itlefef in range(1, 100):
        try:
            qerfeqaerfqe = chrome.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div[' + str(itlefef) + ']/div[2]/h3/a')
            data6777 = qerfeqaerfqe.get_attribute("href")
            listKioooo += [data6777]
        except selenium.common.exceptions.NoSuchElementException:
            pass

    cleanMZEFZFE = []
    for ergzre in listOfRAEA:
        links += [listKioooo[ergzre].replace("uk.", "")]


    # -- COMPARISON & UPLOAD -- #
    uploadToDB("business insider", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "business insider")
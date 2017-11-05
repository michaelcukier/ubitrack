from func.get_data import *

# -- WEBDRIVER -- #
chrome, display = load_chrome()

# def var links
links = []

# -- VOX SCRAPE-- #
try:
    chrome.get("https://www.vox.com/search?order=date&q=basic+income")
    data467657o98 = chrome.find_elements_by_css_selector("h2.c-entry-box--compact__title a")

    listVOXLINKS = []
    listVOXTITLES = []

    for every32000 in data467657o98:
        listVOXTITLES += [every32000.text]
        listVOXLINKS += [every32000.get_attribute("href")]

    voxindex = []
    for liergfzfeezf in listVOXTITLES:
        if ("basic income" in liergfzfeezf) or ("UBI" in liergfzfeezf) or ("Basic Income" in liergfzfeezf) or (
            "Basic income" in liergfzfeezf):
            voxindex += [listVOXTITLES.index(liergfzfeezf)]

    finalListOfLinkVOX = []
    for aergzrthag87 in voxindex:
        links += [listVOXLINKS[aergzrthag87]]

    # -- COMPARISON & UPLOAD -- #
    uploadToDB("vox", links)

    chrome.quit()
    display.stop()

except Exception as e:
    reboot(e, "vox")
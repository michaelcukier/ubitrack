# -*- coding: utf-8 -*-

from selenium import webdriver, common
import selenium
import re
from bs4 import BeautifulSoup
from resizeimage import resizeimage, imageexceptions
from random import randint
import urllib.request
from pyvirtualdisplay import Display
import os
from PIL import ImageEnhance, Image
import PIL
import time
import MySQLdb
import facebook


def send_to_fcb_page(link, titleFcb):
    cfg = {
        "page_id": "1342236565904895",  # Step 1
        "access_token": "EAAEDy7ZBmEeABANxHEZAgxuYTDjEyNUZAiH6zqhBPTqnSv6cMG0Sg4smq57CYZCk7pVjcr78zgGSbZASglxgoh5LiTOxwQruegJFpksZCxHX244vFQUobkmteob6Qo1t2K33ryIlBFF3Hpq3aMz1WOZC36lJih3bdPoMbr3SsD89AZDZD"
    }

    attachment = {
        'link': link,
    }

    api = facebook.GraphAPI(cfg['access_token'])
    po = api.put_wall_post(message=titleFcb, attachment=attachment)


def accessUrl(url, nameUrl):
    try:
        chrome.get(url)
    except selenium.common.exceptions.TimeoutException:
        try:
            chrome.get(url)
        except selenium.common.exceptions.TimeoutException:
            try:
                chrome.get(url)
            except selenium.common.exceptions.TimeoutException:
                print("timeout exception, had to quit " + str(nameUrl))
                chrome.quit()
                display.stop()
                quit()


def cleantime():

    dirtyTime = str(time.ctime())

    dictMonths = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
    }

    getMonth = dirtyTime[4:7]
    for elemDictMonth in dictMonths:
        if elemDictMonth == getMonth:
            getTranslatedMonth = dictMonths.get(elemDictMonth)
            if int(dirtyTime[8:10]) < 10:
                cleanTime = dirtyTime[20:25] + "-" + getTranslatedMonth + "-" + "0" + dirtyTime[9:10] + " " + str(int(int(dirtyTime[11:13]))) + ":" + dirtyTime[14:19]
            else:
                cleanTime = dirtyTime[20:25] + "-" + getTranslatedMonth + "-" + dirtyTime[8:10] + " " + str(int(int(dirtyTime[11:13]))) + ":" + dirtyTime[14:19]

    return cleanTime


def just_connect():
    conn = MySQLdb.connect(host="localhost", user="root", passwd="cukier", db="pythonprogramming")
    c = conn.cursor()

    conn.set_character_set('utf8')
    c.execute('SET NAMES utf8;')
    c.execute('SET CHARACTER SET utf8;')
    c.execute('SET character_set_connection=utf8;')

    return conn, c


def get_current_links():
    conn, c = just_connect()

    c.execute("SELECT * FROM articles;")
    result = c.fetchall()

    list_current_urls = []
    for row in result:
        list_current_urls.append(row[1])

    conn.close()

    return list_current_urls


def load_chrome():
    global chrome
    global display
    display = Display(visible=0, size=(800, 600))
    display.start()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    try:
        chrome = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        return chrome, display
    except ConnectionRefusedError:
        print("HAD TO REBOOT - CAUSE load_chrome()")
        os.system('/sbin/reboot')


def get_unique_title_image_logo(link):
    try:
        chrome.get(link)
    except selenium.common.exceptions.TimeoutException:
        try:
            chrome.get(link)
        except selenium.common.exceptions.TimeoutException:
            theTitle = "pass this one - timeoutexception"
            image = "pass this one - timeoutexception"
            getLogoFomTwitter = "pass this one - timeoutexception"
            getNameFromTwitter = "pass this one - timeoutexception"
            return theTitle, image, getLogoFomTwitter, getNameFromTwitter

    title = chrome.title

    if title != '':
        newTitle = title.split(" ")
        if len(newTitle) != 1:
            perfectTitle = (' '.join(newTitle))
            if " | " in perfectTitle:
                perfectTitle = perfectTitle.split(" | ")
            elif " - " in perfectTitle:
                perfectTitle = perfectTitle.split(" - ")
            elif " – " in perfectTitle:
                perfectTitle = perfectTitle.split(" – ")
            elif " — " in perfectTitle:
                perfectTitle = perfectTitle.split(" — ")
            elif " • " in perfectTitle:
                perfectTitle = perfectTitle.split(" • ")
            elif " · " in perfectTitle:
                perfectTitle = perfectTitle.split(" · ")
            elif " :: " in perfectTitle:
                perfectTitle = perfectTitle.split(" :: ")

            if type(perfectTitle) != list:
                theTitle = perfectTitle
            elif type(perfectTitle) == list:
                theTitle = max(perfectTitle, key=len)
        else:
            theTitle = title
    else:
        theTitle = "no title"

    image = resize_unique_image(grab_unique_image())
    getLogoFomTwitter, getNameFromTwitter = get_unique_logo(link)

    return theTitle, image, getLogoFomTwitter, getNameFromTwitter


def get_unique_logo(link):

    getSource = chrome.page_source
    allLinksFromThePage = re.findall(r'(https?://[^\s]+)', getSource)
    twitterLinks = []

    for eachLink in allLinksFromThePage:
        if ("//twitter.com" in eachLink) or ("//www.twitter.com" in eachLink):
            twitterLinks.append(eachLink)

    try:
        selectFirstLink = twitterLinks[0]
        selectFirstLink = selectFirstLink.replace('"', "")
        selectFirstLink = selectFirstLink.replace('><span', '')
        selectFirstLink = selectFirstLink.replace(",", "")

        chrome.get(selectFirstLink)

        finalLogoURL = chrome.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div[1]/div/a/img')
        getLogoFomTwitter = finalLogoURL.get_attribute("src")
        getNameFromTwitter = chrome.find_element_by_css_selector("a.ProfileHeaderCard-nameLink.u-textInheritColor.js-nav").text
        return getLogoFomTwitter, getNameFromTwitter  # 1st way of getting logo + name, via Twitter

    except (IndexError, selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.WebDriverException):
        chrome.get("https://www.google.co.uk/search?q=" + get_urlclean(link) + "+twitter+profile")
        getAllLinksFromGoogle = chrome.find_elements_by_class_name("_Rm")

        try:
            if "http" not in getAllLinksFromGoogle[0].text:
                chrome.get("http://" + getAllLinksFromGoogle[0].text)
            else:
                chrome.get(getAllLinksFromGoogle[0].text)

        except IndexError:
            return "no_logo.jpg", "no title (twitter)"

        if chrome.current_url == "https://twitter.com/profile?lang=en-gb":
            return "no_logo.jpg", "no title (twitter)"

        try:
            getLogoFomTwitter = chrome.find_element_by_xpath('//*[@id="page-container"]/div[1]/div/div[1]/div[2]/div[1]/div/a/img')
            getLogoFomTwitter = getLogoFomTwitter.get_attribute("src")
            getNameFromTwitter = chrome.find_element_by_css_selector("a.ProfileHeaderCard-nameLink.u-textInheritColor.js-nav").text
            return getLogoFomTwitter, getNameFromTwitter  # 2nd way of getting logo + name, via Twitter & Google

        except selenium.common.exceptions.NoSuchElementException:
            return "no_logo.jpg", "no title (twitter)"


def get_unique_content(link):
    try:
        chrome.get("http://embed.ly/docs/explore/extract")
    except selenium.common.exceptions.TimeoutException:
        chrome.get("http://embed.ly/docs/explore/extract")

    if ("ft.com" != link) and ("forbes.com" != link):
        try:
            findTextBox = chrome.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[1]/div[1]/input")
        except selenium.common.exceptions.NoSuchElementException:
            time.sleep(10)
            chrome.get("http://embed.ly/docs/explore/extract")
            findTextBox = chrome.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[1]/div[1]/input")

        findTextBox.clear()
        findTextBox.send_keys(link)

        findButtonSearch = chrome.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/form/div[1]/div[2]/a/i")
        findButtonSearch.click()

        soup = BeautifulSoup(chrome.page_source, "lxml")
        elem = soup.findAll('div', attrs={'class': 'e e-5'})

        try:
            if len(elem[1]) == 40:
                return "no contefnt"
            else:
                try:
                    return elem
                except UnicodeEncodeError:
                    return "no content"

        except IndexError:
            return "no contefnt"

    else:
        return "no contefnt"


def grab_unique_image():
    c = 0
    webpage = chrome.page_source
    soup2 = BeautifulSoup(webpage, "html5lib")
    img = soup2.find("meta", property="og:image")

    if img:
        imageURL = img["content"].replace("https", "http").replace("//a57", "http://a57").replace("http://images.washingtonpost.com/?url=", "")
        imgName = str(randint(0, 10000)) + "x" + str(randint(0, 10000))

        if ".jpeg" in imageURL:
            imageURL = imageURL.split(".jpeg")
            imageURL = imageURL[0] + ".jpeg"
            whatType = ".jpeg"

        elif ".jpg" in imageURL:
            imageURL = imageURL.split(".jpg")
            imageURL = imageURL[0] + ".jpg"
            whatType = ".jpg"

        elif ".png" in imageURL:
            imageURL = imageURL.split(".png")
            imageURL = imageURL[0] + ".png"
            whatType = ".png"

        elif ".gif" in imageURL:
            imageURL = imageURL.split(".gif")
            imageURL = imageURL[0] + ".gif"
            whatType = ".gif"

        else:
            imageURL = imageURL.split(".jpg")
            imageURL = imageURL[0] + ".jpg"
            whatType = ".jpg"

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        url = imageURL
        local = "/var/www/ubitrack/ubitrack/static/database_images/"
        fileName = str(imgName) + whatType
        try:
            urllib.request.urlretrieve(url, local + fileName)
            return local + fileName
        except (urllib.error.URLError, ValueError):
            return "no image"
    else:
        return "no image"


def resize_unique_image(imgFolderUrl):
    if imgFolderUrl == "no image":
        return "no image"
    else:
        try:
            with open(str(imgFolderUrl), 'r+b') as f:
                with Image.open(f) as image:
                    try:
                        img = imgFolderUrl
                        cover = resizeimage.resize_cover(image, [640, 367])
                        cover.save(img, image.format)
                        imgFolderUrl = imgFolderUrl.split("/")
                        imgFolderUrl = imgFolderUrl[-1]
                        return imgFolderUrl
                    except:
                        try:
                            img = imgFolderUrl
                            cover = resizeimage.resize_cover(image, [484, 277])
                            cover.save(img, image.format)
                            imgFolderUrl = imgFolderUrl.split("/")
                            imgFolderUrl = imgFolderUrl[-1]
                            return imgFolderUrl
                        except:
                            try:
                                img = imgFolderUrl
                                cover = resizeimage.resize_cover(image, [350, 200])
                                cover.save(img, image.format)
                                imgFolderUrl = imgFolderUrl.split("/")
                                imgFolderUrl = imgFolderUrl[-1]
                                return imgFolderUrl
                            except:
                                try:
                                    img = imgFolderUrl
                                    cover = resizeimage.resize_cover(image, [165.9, 95])
                                    cover.save(img, image.format)
                                    imgFolderUrl = imgFolderUrl.split("/")
                                    imgFolderUrl = imgFolderUrl[-1]
                                    return imgFolderUrl
                                except:
                                    return "no image"
        except OSError:
            return "no image"


def makeBrightnessImage(nameImage):
    if nameImage == "no image":
        return "no image"
    else:
        im = Image.open("/var/www/ubitrack/ubitrack/static/database_images/" + nameImage)
        im = im.convert("RGB")

        enhancer = ImageEnhance.Brightness(im)
        im = enhancer.enhance(0.4)

        im.save("/var/www/ubitrack/ubitrack/static/database_images/bright_" + nameImage)
        return nameImage


def get_urlclean(link):
    cleanLink = link.split("//")
    cleanLink = cleanLink[1]
    cleanLink = cleanLink.split("/")
    cleanLink = cleanLink[0].replace("www.", "")

    return cleanLink


def getAllCurentTitles():
    conn, c = just_connect()

    c.execute('SELECT title FROM articles;')
    result = c.fetchall()

    allCurrentTitles = []
    for row in result:
        allCurrentTitles.append(row[0])

    conn.close()

    return allCurrentTitles


def getBlackListUrls():
    conn, c = just_connect()

    c.execute('SELECT url FROM blackList;')
    result = c.fetchall()

    blackListUrls = []
    for row in result:
        blackListUrls.append(row[0])

    conn.close()

    return blackListUrls


def uploadToDB(source, linksBeforeClean):
    linksToAdd = []
    for each in linksBeforeClean:
        if each not in get_current_links():
            if each not in linksToAdd:
                linksToAdd.append(each)

    conn, c = just_connect()

    num = 0
    for link in linksToAdd:
        if link not in getBlackListUrls():
            num += 1
            title, img, getLogoFromTwitter, getNameFromTwitter = get_unique_title_image_logo(link)
            title = str(title)

            if title in getAllCurentTitles():  # check if title already in DB
                num -= 1
                c.execute('INSERT INTO blackList (url) VALUES ("' + str(link) + '")')
                conn.commit()
                print("added one to black list (title already in DB)")
                continue

            img = str(img)
            getLogoFromTwitter = str(getLogoFromTwitter)
            getNameFromTwitter = str(getNameFromTwitter)
            url = str(link)

            if title == "pass this one - timeoutexception":
                c.execute('INSERT INTO blackList (url) VALUES ("' + str(link) + '")')
                conn.commit()
                print("added one to black list (timeout)")
                num -= 1
                continue
            elif title == "no title":
                c.execute('INSERT INTO blackList (url) VALUES ("' + str(link) + '")')
                conn.commit()
                print("added one to black list (no title)")
                num -= 1
                continue

            urlClean = str(get_urlclean(link))
            pubDate = str(cleantime())
            content = str(get_unique_content(link))
            img_bright = makeBrightnessImage(img)

            try:
                c.execute("INSERT INTO articles (title, url, image, URLClean, pubDate, content, mainImage, source, mainImageBrightness, titleOfWebsite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (title, url, getLogoFromTwitter, urlClean, pubDate, content, img, source, img_bright, getNameFromTwitter))
                conn.commit()
            except MySQLdb.OperationalError:
                getNameFromTwitter = "no title (twitter)"
                c.execute("INSERT INTO articles (title, url, image, URLClean, pubDate, content, mainImage, source, mainImageBrightness, titleOfWebsite) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (title, url, getLogoFromTwitter, urlClean, pubDate, content, img, source, img_bright, getNameFromTwitter))
                conn.commit()
            except:
                c.execute('INSERT INTO blackList (url) VALUES ("' + str(link) + '")')
                conn.commit()
                print("added one to black list (couldnt upload to sql db)")
                num -= 1
                continue

            # post to fcb
            try:
                send_to_fcb_page(link, title)
            except facebook.GraphAPIError:
                pass

    if num >= 1:
        print(str(cleantime()) + " - " + source + " - added " + str(num))

    conn.close()


def reboot(exception, nameOfSite):
    print("### - HAD TO REBOOT - PROBLEM: " + str(exception) + " (" + str(nameOfSite) + ")")
    os.system('/sbin/reboot')
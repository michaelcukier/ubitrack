def publish(article):
    published_article = {}
    published_article["url"] = article.url
    published_article["html"] = article.html()
    published_article["urlclean"] = article.urlclean()
    published_article["title"] = article.title()
    published_article["ogimage"] = article.ogimage()
    published_article["mediaLogoAndNameFromTwitter"] = article.mediaLogoAndNameFromTwitter()
    published_article["contentFromEmbdly"] = article.contentFromEmbdly()
    published_article["pubdate"] = article.pubdate()
    return published_article

class Article:

    def __init__(self, url):
        self.url = url

    def html(self):
        if self.url == "http://google.com":
            html = "<html> all google code here </html>"
        return html

    def urlclean(self):
        if self.url == "http://google.com":
            urlclean = "google.com"
        return urlclean
    
    def title(self): # remember to decode in utf8
        if self.html() == "<html> all google code here </html>":
            title = "here's the title from html"
        return title

    def ogimage(self):
        if self.html() == "<html> all google code here </html>":
            ogimage = "here's the og image from html"
        return ogimage

    def mediaLogoAndNameFromTwitter(self):
        if self.url == "http://google.com":
            mediaLogoAndNameFromTwitter = "here's the logo + name from twitter"
        return mediaLogoAndNameFromTwitter

    def contentFromEmbdly(self):
        if self.url == "http://google.com":
            contentFromEmbdly = "clean search engine"
        return contentFromEmbdly

    def pubdate(self):
        return "time now"
    
            
article = Article("http://google.com")  # original article url here

db = publish(article)

print(db)

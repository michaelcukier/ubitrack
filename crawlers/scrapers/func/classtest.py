# get data from url to upload it

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

    def twitterdata(self):
        if self.url == "http://google.com":
            logotwitter = "here's the logo from twitter"
            titletwitter = "here's the title from twitter"
        return logotwitter, titletwitter

    def embedly(self):
        if self.url == "http://google.com":
            embedly = "clean search engine"
        return embedly

    def pubdate(self):
        return "time now"

# tests
article = Article("http://google.com")  # original article url here
for article_data_type in ["html", "urlclean", "title", "ogimage", "twitterdata", "embedly", "pubdate"]:
    print(article_data_type + ": " + str(eval("article." + article_data_type + "()")))

"""
def publish(article): # JSON style output
    published_article = {}
    published_article["url"] = article.url
    for article_data_type in ["html", "urlclean", "title", "ogimage", "twitterdata", "embedly", "pubdate"]:
        published_article[article_data_type] = eval("article." + article_data_type + "()")
    return published_article
"""

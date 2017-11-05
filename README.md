# ubitrack
http://ubitrack.news/ - A website that gathers news articles talking about Basic Income

## Stack
* Built using Python 3
* Using a MySQL database for storing the scraped data
* Deployed on a 1024MB Vultr server on Ubuntu 16.04
* Scripts also posts to the facebook page (https://www.facebook.com/ubi.track.news/) using the Facebook API
* Optimized with Varnish Cache to speed up client loading time of the news aggregator
* Bridge between the scrapers and the front-end is made using Flask

###### Made by Michael Cukier (http://michaelcukier.com)

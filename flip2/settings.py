# Scrapy settings for flip2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import scraper_helper as sh

BOT_NAME = 'flip2'

SPIDER_MODULES = ['flip2.spiders']
NEWSPIDER_MODULE = 'flip2.spiders'
DEFAULT_REQUEST_HEADERS = sh.get_dict(
''' 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: T=TI163370120936000277486848514475124610075523076949565426879817975590; SN=VI58B38FAF07CB42F89DA4DCA3FD699813.TOKF3352FE715F642D2B920E0BC0827737D.1633701209.LO; Network-Type=4g; pxcts=2004f810-283f-11ec-bbc9-2bb0df5be8d5; _pxvid=2004a998-283f-11ec-b52e-454854656d65; _pxff_ddtc=1; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; S=d1t16PwQ/P2h3P3A/Pws/HT9qPxJcBD3xT3hcAkRP0ChrAlgyEUQdStIrBYvykLq0HL2NGrc+xPJOLASeuZ3G7X8IiQ==; qH=eb4af0bf07c16429; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18909%7CMCMID%7C72105741949827621636008155679483169213%7CMCAID%7CNONE%7CMCAAMLH-1634306004%7C12%7CMCAAMB-1634306005%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1633708405s%7CNONE; _px3=af5c552bf9d07abe6d6d800d398507602ba55983c4d688db248a956175fe2943:lBTVFYl3Tv6S7cV0Cge1E6d6HPqL4b+oD5mprJS2dbWFUD25CnMwRF0S2mdSnpxQAcd8UDSt8x27oMLwyucm9Q==:1000:QTfNV4MJ2nuvfvEGWBcLMADq1GGuDy2vo2qxQNDpkznzsdUGipO1mSIs3Ev4WYpWWCID0PE4YzqiCb9vHIR3ObdB7fqiBF4SzdJK0IFEmsSb/XEuRx2q0V4x7LVnJFDynVZhx0rxqopbXvctiPE/s9xJQmzZAyBxnBKE9M/jGsMNHxxgvd9VDU4JFw6YFoDGYGCAwapDlX0lj6G2j8+/fw==
Host: www.flipkart.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36
'''
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'flip2 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Name of the file where data extracted is stored
#File is saved as as a csv format. to change it into jason use .json as extention
#FEED_URI = "testfile1.csv"



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

#{
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'flip2.middlewares.Flip2SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'flip2.middlewares.Flip2DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'flip2.pipelines.Flip2Pipeline': 300,
}

#ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
#IMAGES_STORE = 'local_folder'



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

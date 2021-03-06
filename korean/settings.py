# -*- coding: utf-8 -*-

# Scrapy settings for korean project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import pymysql
BOT_NAME = 'korean'

SPIDER_MODULES = ['korean.spiders']
NEWSPIDER_MODULE = 'korean.spiders'
MYSQL_DB = 'frequentwords'
MYSQL_HOST = '127.0.0.1'
MYSQL_user = 'root'
MYSQL_TABLE = 'zh_full'
MYSQL_PASSWORD = '18351962092'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'korean (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

SPLASH_URL = 'http://localhost:8051'
DOWNLOADER_MIDDLEWARES={
'scrapy_splash.SplashCookiesMiddleware': 100,
'scrapy_splash.SplashMiddleware': 200,
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 300,}
DUPERFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
SPIDER_MIDDLEWARES={'scrapy_splash.SplashDeduplicateArgsMiddleware': 100}
# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'korean.middlewares.KoreanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'korean.middlewares.KoreanDownloaderMiddleware': 543,
    'korean.middlewares.HttpProxyMiddleware': 300,
 }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'korean.pipelines.KoreanPipeline': 300,
}
HEADERS ={'Accept':  'text/html, */*; q=0.01',
'Accept-Encoding':  'gzip, deflate, br',
'Accept-Language':  'zh-CN,zh;q=0.9',
'Alldict-Locale':  'zh_CN',
'Connection':  'keep-alive',
'Cookie':  'npic=oJqmTY+fgfcJ2wOohl3EuWuiJD/cbl/uExb8862C94dWgl5JxHSJ2ZPYQ2s8vKXyCA==; NNB=QQ2WGQFCHQ6FY; JSESSIONID=A5B581DE3FD3ED0EB43FD80049F870FB',
'Host':  'korean.dict.naver.com',
'Referer':  'https://korean.dict.naver.com/kozhdict/',
'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'X-Requested-With':  'XMLHttpRequest',}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

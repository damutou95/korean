# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from korean import settings
from korean.items import KoreanItem
import json
from urllib import parse
import logging
import pymysql
import random

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    #allowed_domains = ['sss']
    headers = settings.HEADERS
    host = settings.MYSQL_HOST
    user = settings.MYSQL_user
    password = settings.MYSQL_PASSWORD
    dbname = settings.MYSQL_DB
    table = settings.MYSQL_TABLE

    #在这里输入一系列想要翻译的文本
    #测试 ts = ['你好', '明天']
    db = pymysql.connect(host=host, user=user, passwd=password, db=dbname)
    cursor = db.cursor()
    sql = f"select * from {table}"
    cursor.execute(sql)
    results = cursor.fetchall()
    start_urls = []
    for row in results:
        word = row[0]
        keyword = parse.quote(word)
        start_urls.append('https://korean.dict.naver.com/cndictApi/search/example?sLn=zh_CN&q={}&mode=mobile&pageNo=1&format=json&pageCon=vlive'.format(keyword))

    def start_requests(self):
        for i in self.start_urls:
            yield Request(url=i, callback=self.parse, headers=self.headers, meta={'keyword': self.keyword, 'tag': 0})

    #获取字幕第一页中的总页数来判断是否进行全部抓取，如果页数大于100就只爬取一百页
    def parse(self, response):
        results = json.loads(response.text)
        pageNum = results['searchVliveResults']['totalPage']
        pageInfo = results['searchVliveResults']['searchVLiveList']
        #如果没有词条的相关字幕，则返回为空，我们设置为零
        pageNumneed = 0
        if pageInfo !=[]:
            if pageNum <= 100 and pageNum > 0:
                pageNumneed = pageNum
            elif pageNum > 100:
                pageNumneed = 100
            print(pageNumneed)
            print('4444444444444444444444')
            logging.info('#####################################################第一页完成')
            for i in range(pageNumneed):
                page = i+1
                host = '127.0.0.1'
                user = 'root'
                passwd = '18351962092'
                dbname = 'proxies'
                tablename = 'proxy'
                proxies = []
                db = pymysql.connect(host, user, passwd, dbname)
                cursor = db.cursor()
                sql = f"select * from {tablename}"
                cursor.execute(sql)
                results = cursor.fetchall()
                cursor.close()
                for row in results:
                    ip = row[0]
                    port = row[1]
                    fromUrl = f"http://{ip}:{port}"
                    proxies.append(fromUrl)
                proxy = random.choice(proxies)
                url = response.url.replace('pageNo=1', f'pageNo={str(page)}')
                dbname2 = 'koreanUrl'
                tablename2 = 'url'
                db2 = pymysql.connect(host, user, passwd, dbname2)
                cursor2 = db2.cursor()
                sql2 = f"select * from {tablename2}"
                cursor2.execute(sql2)
                results2 = cursor2.fetchall()
                db2.commit()
                cursor2.close()
                db2.close()
                urls = []
                for row in results2:
                    urls.append(row[0])
                if url not in urls:
                    yield Request(url=url, callback=self.parse_item, headers=self.headers, meta={'proxy': proxy, 'pageNum': page, 'tag': 0}, dont_filter=True)

    def parse_item(self, response):
        results = json.loads(response.text)
        lists = results['searchVliveResults']['searchVLiveList']
        for list in lists:
            item = KoreanItem()
            item['kr'] = list['krSubtitle'].replace('<b>', '').replace('</b>', '').replace(r"\"", "\"").replace("\"", r"\"").replace(r"\'", "'").replace("'", r"\'")
            item['en'] = list['enSubtitle'].replace('<b>', '').replace('</b>', '').replace(r"\"", "\"").replace("\"", r"\"").replace(r"\'", "'").replace("'", r"\'")
            item['cn'] = list['foSubtitle'].replace('<b>', '').replace('</b>', '').replace(r"\"", "\"").replace("\"", r"\"").replace(r"\'", "'").replace("'", r"\'")
            item['video'] = list['videoTitle'].replace(r"\"", "\"").replace("\"", r"\"").replace(r"\'", "'").replace("'", r"\'")
            logging.info('#####################################成功读取一条翻译#####################################')
            print(item)
            yield item
        logging.info(f"#####################################################成功爬取了第{str(response.meta['pageNum'])}页")




# -*- coding: utf-8 -*-
import hashlib
import pymysql
import time
from pymysql.err import InternalError,IntegrityError
from pymysql import cursors
from twisted.enterprise import adbapi
import logging

class KoreanPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls, settings):
        dbparas = dict(
            host = '127.0.0.1',
            user = 'root',
            password = '18351962092',
            db = 'korean',
            charset = 'utf8',
            cursorclass = cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparas)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.doInsert, item)
        query.addErrback(self.handleError)
        return item

    def handleError(self, failure):
        print(failure)

    def doInsert(self, cursor, item):
        s = item['en'] + item['cn'] + item['kr']
        hash = hashlib.md5()
        hash.update(s.encode('utf-8'))
        hashCode = hash.hexdigest()
        try:
            sql = f"""insert into fanyi(en,cn,kr,video,hashCode,crawlTime,spider) values("{item['en']}","{item['cn']}","{item['kr']}","{item['video']}","{hashCode}","{time.strftime('%Y-%m-%d',time.localtime())}","fanyi")"""
            cursor.execute(sql)
        except InternalError:
            logging.info("################成功过滤emoji！###############")
        except IntegrityError:
            logging.info("################成功过滤重复结果！################")



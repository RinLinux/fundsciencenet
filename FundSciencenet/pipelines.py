# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class FundsciencenetPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlTwistedPipeline(object):
    # 使用Twisted异步储存
    def __init__(self,dbpool):
        self.dbpool = dbpool


    @classmethod
    def from_settings(cls,settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            database = settings['MYSQL_DB'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)


    def process_item(self,item,spider):
        # 异步执行mysql插入操作
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)


    def handle_error(self,failure):
        #处理异步插入的异常
        print(failure)


    def do_insert(self,cursor,item):
            # 执行具体操作
        insert_sql = """
            insert into fundsciencenet_infor(url,url_object_id,title,approval_number,subject_classification,
            project_leader,title_of_leader,dependent_unit,subsidized_amount,project_category,time_start,time_end,
            chinese_keywords,english_keywords,chinese_abstract,english_abstract,summary_abstract)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert_sql,(item['url'],item['url_object_id'],item['title'],item['approval_number'],
                                  item['subject_classification'],item['project_leader'],item['title_of_leader'],
                                   item['dependent_unit'],item['subsidized_amount'],item['project_category'],
                                   item['time_start'],item['time_end'],item['chinese_keywords'],
                                   item['english_keywords'],item['chinese_abstract'],item['english_abstract'],
                                  item['summary_abstract']))



    # url = scrapy.Field()
    # url_object_id = scrapy.Field()
    # title = scrapy.Field()
    # approval_number = scrapy.Field()
    # subject_classification = scrapy.Field()
    # project_leader = scrapy.Field()
    # title_of_leader = scrapy.Field()
    # dependent_unit = scrapy.Field()
    # subsidized_amount = scrapy.Field()
    # project_category = scrapy.Field()
    # time_start = scrapy.Field()
    # time_end = scrapy.Field()
    # chinese_keywords = scrapy.Field()
    # english_keywords = scrapy.Field()
    # chinese_abstract = scrapy.Field()
    # english_abstract = scrapy.Field()
    # summary_abstract = scrapy.Field()
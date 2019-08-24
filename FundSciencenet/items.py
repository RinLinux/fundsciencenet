# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from scrapy.loader import ItemLoader



class FundsciencenetItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class FundsciencenetItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    title = scrapy.Field()
    approval_number = scrapy.Field()
    subject_classification = scrapy.Field()
    project_leader = scrapy.Field()
    title_of_leader = scrapy.Field()
    dependent_unit = scrapy.Field()
    subsidized_amount = scrapy.Field()
    project_category = scrapy.Field()
    time_start = scrapy.Field()
    time_end = scrapy.Field()
    chinese_keywords = scrapy.Field()
    english_keywords = scrapy.Field()
    chinese_abstract = scrapy.Field()
    english_abstract = scrapy.Field()
    summary_abstract = scrapy.Field()


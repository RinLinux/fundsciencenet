# -*- coding: utf-8 -*-
import scrapy
from items import FundsciencenetItem, FundsciencenetItemLoader
from scrapy import Request
from utils.common import get_md5


class FundsciencenetSpider(scrapy.Spider):
    name = 'fundsciencenet'
    allowed_domains = ['fund.sciencenet.cn']
    start_urls = ['http://fund.sciencenet.cn/search?submit=list&page=31']

    # "http://fund.sciencenet.cn/search?yearStart=2019&filter%5Bsubject%5D%5B0%5D=C&submit=list&page=1"

    def parse(self, response):

        post_urls = response.css('.item .t a::attr(href)').extract()
        for url in post_urls:
            yield Request(url=url, callback=self.parse_detail)

        next_url = response.css('.result_num p span a::attr(href)').extract()[-1]
        if next_url:
            yield Request(url=next_url,callback=self.parse)

    def parse_detail(self, response):

        item_loader = FundsciencenetItemLoader(item=FundsciencenetItem(), response=response)

        item_loader.add_css('title','.v_con h1::text')
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id',get_md5(response.url))
        content_vcon = response.xpath('//*[@class="v_con"]/table/tr/td')
        item_loader.add_value('approval_number', content_vcon[0].xpath('text()').extract_first(''))
        item_loader.add_value('subject_classification', content_vcon[1].xpath('text()').extract_first(''))
        item_loader.add_value('project_leader', content_vcon[2].xpath('text()').extract_first(''))
        item_loader.add_value('title_of_leader', content_vcon[3].xpath('text()').extract_first('NA'))
        item_loader.add_value('dependent_unit', content_vcon[4].xpath('text()').extract_first(''))
        item_loader.add_value('subsidized_amount', content_vcon[5].xpath('text()').extract_first(''))
        item_loader.add_value('project_category', content_vcon[6].xpath('text()').extract_first('NA'))
        item_loader.add_value('time_start', response.xpath('//*[@class="v_con"]/table/tr[3]/td[3]/text()[1]').extract_first(''))
        item_loader.add_value('time_end', response.xpath('//*[@class="v_con"]/table/tr[3]/td[3]/text()[2]').extract_first(''))
        item_loader.add_value('chinese_keywords',content_vcon[8].xpath('text()').extract_first('NA'))
        item_loader.add_value('english_keywords',content_vcon[9].xpath('text()').extract_first('NA'))

        content_usual = response.xpath('//*[@class="usual"]/div/table/tr/td')
        item_loader.add_value('chinese_abstract',content_usual[0].xpath('text()').extract_first('NA'))
        item_loader.add_value('english_abstract',content_usual[1].xpath('text()').extract_first('NA'))
        item_loader.add_value('summary_abstract',content_usual[2].xpath('text()').extract_first('NA'))
        fundsciencenet_item = item_loader.load_item()
        yield fundsciencenet_item



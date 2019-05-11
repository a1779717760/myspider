# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['http://hr.tencent.com/position.php']
    start_urls = ['http://http://hr.tencent.com/position.php/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy
from ..items import YnzpItem


class YnzpwSpider(scrapy.Spider):
    name = 'ynzpw'
    def start_requests(self):
        num = 3000
        while True:
            url = 'http://www.ynzp.com/cms/personsearch.html?page=' + str(num)
            num += 1
            print('正在安排第',num,'页')
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        item= YnzpItem()
        for i in range(0, 20):
            item['name'] = response.xpath('//dl[@class="w700"]/dt/em/a/text()').extract()[i][:3]
            item['job'] = response.xpath('//dl[@class="w700"]/dt/em/a/text()').extract()[i][8:].strip()[:-2]

            item['sex'] = response.xpath('//dl[@class="w700"]/dd[1]/text()').extract()[i].split('|')[0]
            item['age'] = response.xpath('//dl[@class="w700"]/dd[1]/text()').extract()[i].split('|')[1]
            item['height'] = response.xpath('//dl[@class="w700"]/dd[1]/text()').extract()[i].split('|')[2]
            item['marriage'] = response.xpath('//dl[@class="w700"]/dd[1]/text()').extract()[i].split('|')[3]
            item['education'] = response.xpath('//dl[@class="w700"]/dd[1]/text()').extract()[i].split('|')[4]
            item['Intention_job'] = response.xpath('//dl[@class="w700"]/dd[2]/text()').extract()[i][5:]
            print( item['name'] ,item['job'] ,item['sex'] ,item['age'] ,item['height'] ,item['marriage'] ,item['education'],item['Intention_job'] )
            yield item

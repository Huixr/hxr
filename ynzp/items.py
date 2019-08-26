# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YnzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    sex= scrapy.Field()
    height= scrapy.Field()
    marriage= scrapy.Field()
    education= scrapy.Field()
    job= scrapy.Field()
    Intention_job= scrapy.Field()

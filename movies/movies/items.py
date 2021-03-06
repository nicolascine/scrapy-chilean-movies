# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MoviesItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    duration = scrapy.Field()
    format = scrapy.Field()
    type = scrapy.Field()
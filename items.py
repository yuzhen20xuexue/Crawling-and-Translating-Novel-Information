# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Myscrapy3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Commentltem(scrapy.Item):

    Novel = scrapy.Field()
    Novel_style = scrapy.Field()
    Author = scrapy.Field()
    Publication_date = scrapy.Field()
    Score = scrapy.Field()
    Read_times = scrapy.Field()
    New_page = scrapy.Field()
    Introduction = scrapy.Field()


# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    basic_price = scrapy.Field()
    discount_price = scrapy.Field()
    rating = scrapy.Field()
    _id = scrapy.Field()


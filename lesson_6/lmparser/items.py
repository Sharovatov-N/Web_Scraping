# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


def price_to_float(price):
    if price:
        return float(price.replace(' ', ''))
    return price


def clean_string(asd):
    if asd:
        return asd.replace('\n', '').rstrip().lstrip()
    return asd


class LmparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(price_to_float), output_processor=TakeFirst())
    photo = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst())
    keys = scrapy.Field()
    values = scrapy.Field(input_processor=MapCompose(clean_string))
    specifications = scrapy.Field()
    _id = scrapy.Field()

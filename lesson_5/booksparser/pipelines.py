# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
import re

class BooksparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.books

    def process_item(self, item, spider):
        if spider.name == 'labirint':
            name = item['name']
            name = re.split(r':', name)
            item['name'] = name[-1]

        if item['rating']:
            rating = item['rating']
        else:
            item['rating'] = '0'

        if item['basic_price']:
            basic_price = item['basic_price']
            basic_price = re.split(r' ', basic_price)
            item['basic_price'] = basic_price[0]
        else:
            item['basic_price'] = 'Скидки нет'

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        return item

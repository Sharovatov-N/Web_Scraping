import scrapy
from scrapy.http import HtmlResponse
from lmparser.items import LmparserItem
from scrapy.loader import ItemLoader


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}&suggest=true']

    def parse(self, response: HtmlResponse):

        ads_links = response.xpath("//a[@class= 'plp-item__info__title']")

        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

        next_page = response.xpath("//a[@navy-arrow='next']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LmparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('price', '//span[@slot = "price"]/text()')
        loader.add_xpath('photo', "//img[@alt='product image']/@src")
        loader.add_xpath('keys', "//div[@class='def-list__group']//dt/text()")
        loader.add_xpath('values', "//div[@class='def-list__group']//dd/text()")
        loader.add_value('url', response.url)

        yield loader.load_item()

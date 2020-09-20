import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem

class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/catalog/izuchenie-inostrannykh-yazykov-1788/']

    def parse(self, response:HtmlResponse):

        books = response.css("div.book__title a.book__title-link::attr(href)").extract()
        for book in books:
            yield response.follow(book, callback=self.book_parse)

        next_page = response.css("a.catalog-pagination__item._text.js-pagination-catalog-item::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def book_parse(self, response:HtmlResponse):

        name = response.css("h1::text").extract_first()
        link = response.url
        author =response.css("div.js-tab-switcher-item._active a.item-tab__chars-link::text").extract_first()
        basic_price = response.css("div.item-actions__price-old::text").extract_first()
        discount_price = response.css("div.item-actions__price b::text").extract_first()
        rating = response.css("span.rating__rate-value::text").extract_first()

        yield BooksparserItem(name=name, link=link, author=author, basic_price=basic_price, discount_price=discount_price, rating=rating)
        print()
        



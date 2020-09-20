import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/религия/?stype=0&russianonly=1']

    def parse(self, response: HtmlResponse):

        books = response.css("div.product-cover a.product-title-link::attr(href)").extract()
        for book in books:
            yield response.follow(book, callback=self.book_parse)

        next_page = response.css(
            "a.pagination-next__text::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def book_parse(self, response: HtmlResponse):

        name = response.css("h1::text").extract_first()
        link = response.url
        author = response.css("div.authors a.analytics-click-js::text").extract_first()
        basic_price = response.css("span.buying-priceold-val-number::text").extract_first()
        discount_price = response.css("span.buying-pricenew-val-number::text").extract_first()
        rating = response.xpath("//div[@id='rate']/text()").extract_first()

        yield BooksparserItem(name=name, link=link, author=author, basic_price=basic_price, discount_price=discount_price, rating=rating)
        print()

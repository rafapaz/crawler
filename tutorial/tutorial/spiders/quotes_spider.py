import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').getall()
        autors = response.xpath('//div[@class="quote"]/span/small[@class="author"]/text()').getall()
        for q, a in zip(quotes, autors):
            yield {
                'quote': q,
                'author': a,                
            }
        
        for a in response.xpath('//ul[@class="pager"]/li[@class="next"]/a'):
            yield response.follow(a, callback=self.parse)

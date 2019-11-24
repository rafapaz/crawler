import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for a in response.xpath('//div[@class="quote"]/span/a'):
            yield response.follow(a, self.parse_author)
        
        for a in response.xpath('//ul[@class="pager"]/li[@class="next"]/a'):
            yield response.follow(a, callback=self.parse)
    
    def parse_author(self, response):
        author = response.xpath('//div[@class="author-details"]/h3/text()').get()
        born = response.xpath('//div[@class="author-details"]/p/span[@class="author-born-date"]/text()').get()
        desc = response.xpath('//div[@class="author-details"]/div[@class="author-description"]/text()').get()

        yield {                
                'author': author,
                'born': born,
                'description': desc,
            }
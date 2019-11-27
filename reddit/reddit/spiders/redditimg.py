# -*- coding: utf-8 -*-
import scrapy


class RedditimgSpider(scrapy.Spider):
    name = 'redditimg'
    start_urls = ['http://https://www.reddit.com/']

    def parse(self, response):
        links = response.xpath('//img/@src')
        html = ''

        for link in links:
            # Extract the URL text from the element
            url = link.get()
            # Check if the URL contains an image extension
            if any(extension in url for extension in ['.jpg', '.gif', '.png']):
                html += '''
                < a href="{url}" target="_blank">
                    < img src="{url}" height="33%" width="33%" />
                < /a>
                '''.format(url=url)

        # Open an HTML file, save the results
        with open('frontpage.html', 'a') as page:
            page.write(html)
            # Close the file
            page.close()

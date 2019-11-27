# -*- coding: utf-8 -*-
import scrapy
from re import sub
from decimal import Decimal

def convert_money(money):
    return Decimal(sub(r'[^\d.]', '', money))

class PriceSpider(scrapy.Spider):
    name = 'price'
    start_urls = ['http://https://www.amazon.com/s?k=python/']

    def parse(self, response):
        prices = response.css('.a-price .a-offscreen::text').getall()
        stats = dict()
        values = []

        for price in prices:
            value = convert_money(price)
            values.append(value)
        
        values.sort()

        # Calculate price statistics
        stats['average_price'] = round(sum(values) / len(values), 2)
        stats['lowest_price'] = values[0]
        stats['highest_price'] = values[-1]
        stats['total_prices'] = len(values)

        print(stats)
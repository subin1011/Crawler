import scrapy
import selectorlib
import os
import json
from urllib.parse import urlencode
from urllib.parse import urljoin


class AmazonInSpider(scrapy.Spider):
    name = 'AmazonIn'
    base_url = 'https://www.amazon.in/'
    allowed_domains = ['amazon.in']
    queries = ['snacks']

    # Create Extractor for listing page
    listing_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yaml/amazon_in/ListingPage.yml'))
    # Create Extractor for product page
    product_page_extractor = selectorlib.Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__),'../selectorlib_yaml/amazon_in/ProductPage.yml'))

    # List page output file
    listing_page_output_file = os.path.join(os.path.dirname(__file__),'../output/amazon_in/ListingPageOutput.jsonl')
    # Product page output file
    product_page_output_file = os.path.join(os.path.dirname(__file__),'../output/amazon_in/ProductPageOutput.jsonl')

    def start_requests(self):
        for query in self.queries:
            url = 'https://www.amazon.in/s?' + urlencode({'k': query})
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extract data using Extractor
        data = self.listing_page_extractor.extract(response.text)
        self.write_to_file(self.listing_page_output_file, data)
        if 'next_page' in data:
            yield scrapy.Request(data['next_page'], callback=self.parse)
        for p in data['products']:
            url = urljoin(self.base_url, p['url'])
            yield scrapy.Request(url, callback=self.parse_product)

    def parse_product(self, response):
        # Extract data using Extractor
        product = self.product_page_extractor.extract(response.text)
        if product:
            self.write_to_file(self.product_page_output_file, product)
            yield product

    def write_to_file(self, file, data):
        with open(file,'a') as outfile:
            if data:
                json.dump(data, outfile)
                outfile.write("\n")

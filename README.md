# Crawler
A Web crawler, using [Scrapy](https://scrapy.org/) and [Selectorlib](https://pypi.org/project/selectorlib/).

## To start crawling Amazon.in
Currently supporting static url alone. Add or Modify the search urls [here](https://github.com/subin1011/Crawler/blob/master/crawler/spiders/AmazonIn.py#L12)
Command to start crawling Amazon Product lists and details
```bash
cd <path/to/the/crawler/project>
scrapy crawl AmazonIn
```

# Crawler
A Web crawler, using [Scrapy](https://scrapy.org/) and [Selectorlib](https://pypi.org/project/selectorlib/).

## Setup
Install Python3 if not already installed.
```bash
git clone https://github.com/subin1011/Crawler.git
cd Crawler
python3 -m venv crawler-env # Recommended to create a venv
source crawler-env/bin/activate
pip install -r required_packages.txt
```

## To start crawling Amazon.in
Currently supporting static queries alone. Add or Modify the search queries [here](https://github.com/subin1011/Crawler/blob/master/crawler/spiders/AmazonIn.py#L12).

Command to start crawling Amazon Product lists and details
```bash
cd <path/to/the/crawler/project>
scrapy crawl AmazonIn
```

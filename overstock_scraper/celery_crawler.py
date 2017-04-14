import sys

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from overstock_scraper.spiders.overstock_spider import OverstockSpider

def scrape_module():
    crawler = CrawlerProcess(get_project_settings())
    crawler.crawl(OverstockSpider, task_id=sys.argv[1])
    crawler.start()

if __name__ == '__main__':
    scrape_module()
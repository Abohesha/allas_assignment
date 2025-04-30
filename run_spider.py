from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products import ProductsSpider

process = CrawlerProcess(get_project_settings())
process.crawl(ProductsSpider)
process.start()

BOT_NAME = "kallofem_scraper"

SPIDER_MODULES = ["kallofem_scraper.spiders"]
NEWSPIDER_MODULE = "kallofem_scraper.spiders"

FEEDS = {
    "output/products.json": {"format": "json", "overwrite": True},
}
ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = "utf-8"

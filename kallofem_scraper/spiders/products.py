import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"

    def __init__(self, url=None, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [url] if url else []

    allowed_domains = ["kallofem.hu"]
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        for product in response.css("article.product-row"):
            name = product.css("h4::text").get()
            price = product.css("span.product-price::text").get()
            image_url = product.css("img::attr(src)").get()

            if name and price and image_url:
                yield {
                    "name": name.strip(),
                    "price": price.strip(),
                    "image_url": response.urljoin(image_url)
                }

        next_page = response.css("li.page-item a[rel='next']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)




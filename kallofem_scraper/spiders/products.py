import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["kallofem.hu"]
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        for product in response.css("article.product-row"):
            name = product.css("h4::text").get()
            price = product.css("div.product-more-text::text").get()
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

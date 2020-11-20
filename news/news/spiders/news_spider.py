import scrapy

class NewsSpider(scrapy.Spider):
    name = "snopes_crawler"
    allowed_domains = ["snopes.com/fact-check"]
    start_urls = ["https://www.snopes.com/fact-check/woody-allen-dead-hoax/"]

    def parse(self,response):
        with open("result.txt","w") as f:
            f.write(response.css('date-published').get())
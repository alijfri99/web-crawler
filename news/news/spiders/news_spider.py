import scrapy
from w3lib.html import remove_tags

class NewsSpider(scrapy.Spider):
    name = "snopes_crawler"
    allowed_domains = ["snopes.com/fact-check"]
    start_urls = ["https://www.snopes.com/fact-check/florida-man-pole-car-roof/","https://www.snopes.com/fact-check/2020-election-over/"]

    def parse(self,response):
        title = response.xpath("//h1/text()").get() #getting the title
        url = response.url #getting the url
        contents = remove_tags(response.xpath("//div[@class='content']").get()) #getting the contents
        date = response.xpath("//span[@class='date date-published']/text()").get() #getting the publish date
        label = response.xpath("//h5[contains(@class,'rating-label')]/text()").get() #getting the label
        author = response.xpath("//a[@class='author']/text()").get() #getting the author
        claim = response.xpath("//div[@class='claim']/p/text()").get() #getting the claim


        yield {
            'title' : title,
            'url' : url,
            'contents' : contents,
            'date' : date,
            'label' : label,
            'author' : author,
            'claim' : claim
        }
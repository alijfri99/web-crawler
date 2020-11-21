import scrapy
from w3lib.html import remove_tags


class NewsSpider(scrapy.Spider):
    name = "snopes_crawler"
    allowed_domains = ["snopes.com/fact-check"]
    start_urls = ["https://www.snopes.com/fact-check/"]
    visited_urls = []

    def parse_post(self,response):
        title = response.xpath("//h1/text()").get()  # getting the title
        url = response.url  # getting the url
        contents = remove_tags(response.xpath("//div[@class='content']").get())  # getting the contents
        date = response.xpath("//span[@class='date date-published']/text()").get()  # getting the publish date
        label = response.xpath("//h5[contains(@class,'rating-label')]/text()").get()  # getting the label
        author = response.xpath("//a[@class='author']/text()").get()  # getting the author
        claim = response.xpath("//div[@class='claim']/p/text()").get()  # getting the claim

        yield {
            'title': title,
            'url': url,
            'contents': contents,
            'date': date,
            'label': label,
            'author': author,
            'claim': claim
        }

    def parse(self, response):
        posts = response.xpath("//a[contains(@class,'media post')]/@href").getall()
        for post in posts:
            if post not in self.visited_urls:
                self.visited_urls.append(post)
                yield scrapy.Request(post,callback=self.parse_post,dont_filter=True)
        next_page = response.xpath("//a[@class='btn-next btn']/@href").get()
        if next_page is not None:
            yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)



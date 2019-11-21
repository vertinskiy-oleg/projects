import scrapy
from time import sleep

class LinksSpider(scrapy.Spider):
    name = 'links_spider'
    start_urls = ['https://qarea.com/blog']

    def parse(self, response):
        for post_url in response.css('.post h3>a::attr(href)'):
            yield response.follow(post_url, self.parse_post)

    def parse_post(self, response):
        for a in response.css('div.article-content-main p > a'):
            yield {
                'post_title': response.css('h1::text').get(),
                'post_url': response.css('link[rel=canonical]::attr(href)').get(),
                'link_url': a.css('a::attr(href)').get(),
                'link_text': a.css('a::text').get()
            }


        # next = response.css('a.next::attr(href)').get()
        # if next:
        #     yield response.follow(next, self.parse)
        #     sleep(1)

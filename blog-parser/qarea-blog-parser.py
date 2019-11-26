import scrapy
from time import sleep

class LinksSpider(scrapy.Spider):
    name = 'links_spider'
    start_urls = ['https://qarea.com/blog']

    ###Parsing posts url and following them calling parse_post method
    def parse(self, response):
        for post_url in response.css('.post h3>a::attr(href)'):
            yield response.follow(post_url, self.parse_post)

        ###Following second page. Need to change selector to ('a.next::attr(href)') to parse the next page.
        # next = response.css('a.next::attr(href)').get()
        # if next:
        #     sleep(2)
        #     yield response.follow(next, self.parse)

    ###Method for parsing posts
    def parse_post(self, response):
        for a in response.css('div.article-content-main p  a'):
            yield {
                'pub_date': response.css('div.article-head-date > span::text').get(),
                'post_title': response.css('h1::text').get(),
                'post_url': response.url,
                'link_url': response.urljoin(a.css('a::attr(href)').get()),
                ###If for checking text in a tag (with span tag or without)
                'link_text': a.css('a span::text').get() if a.css('a span::text') else a.css('a::text').get()
            }

        
    


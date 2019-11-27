import scrapy
from time import sleep

class LinksSpider(scrapy.Spider):
    name = 'links_spider'
    start_urls = ['https://testfort.com/blog']

    #Parsing posts url and following them calling parse_post method
    def parse(self, response):
        for post_url in response.css('.post h3>a::attr(href)'):
            sleep(1)
            yield response.follow(post_url, self.check_no_links)

        #Following second page. Need to change selector to ('a.next::attr(href)') to parse the next page.
        next = response.css('a.next::attr(href)').get()
        if next:
            yield response.follow(next, self.parse)

    #Method for parsing posts
    def parse_post(self, response):
        for a in response.css('div.entry-content p  a'):
            yield {
                'pub_date': response.css('span.date::text').get(),
                'post_title': response.css('h1::text').get(),
                'post_url': response.url,
                'link_url': response.urljoin(a.css('a::attr(href)').get()),
                #If for checking text in a tag (with span or strong or b tag or without)
                'link_text': a.css('a span::text').get() or a.css('a strong::text').get() or a.css('a b::text').get() 
                            if a.css('a span') or a.css('a strong') or a.css('a b') else a.css('a::text').get()
            }

    #Method for checking posts without links in content
    def check_no_links(self, response):
        if not response.css('div.entry-content p  a'):
            yield {
                'pub_date': response.css('span.date::text').get(),
                'post_title': response.css('h1::text').get(),
                'post_url': response.url
            }    
    
    


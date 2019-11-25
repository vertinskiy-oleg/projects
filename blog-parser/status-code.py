import scrapy

class StatusCodeSpider(scrapy.Spider):
    name = 'status_spider'
    start_urls = ['https://qarea.com/blog/who-runs-microservices-devops']
    handle_httpstatus_list = [404]

    def parse(self, response):
        for url in response.css('div.article-content-main p  a::attr(href)'):
            yield response.follow(url, self.parse_status_code)

    def parse_status_code(self, response):
        yield {
            'url': response.url,
            'status': response.status
        }
from requests_html import HTMLSession

url = 'https://www.upwork.com/search/jobs/?q=python&sort=recency'

session = HTMLSession()

response = session.get(url)

jobs = response.html.xpath("//section[@data-ng-if='!loadingSpinner']//h4//up-c-line-clamp")

for html in response.html:
    print(html)

# for job in jobs:
#     print(job.text)

breakpoint()
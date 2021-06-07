import scrapy


class QuotesSpider(scrapy.Spider):
    name = "headline_crawl"
    start_urls = []
    for i in range(1, 1247):
        start_urls.append('https://www.betootaadvocate.com/page/' + str(i) + '/?s')
    
    

    def parse(self, response):
        for main_content in response.css('div.td-ss-main-content'):
            for quote in main_content.css('div.item-details'):
                for h3 in quote.css('div.item-details'):
                    yield {
                        "article_link": h3.css('a::attr(href)').get(),
                        'headline': h3.css('a::text').get(),
                        "is_sarcastic": 1,

                    }
import scrapy


class ImdbSpiderSpider(scrapy.Spider):
    name = "imdb_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        imdb_scrapes=response.css('div.ipc-metadata-list-summary-item__c')
        for imdb_scrape in imdb_scrapes:
            yield {
                'title':imdb_scrape.css('a h3.ipc-title__text::text').get(),
                 'Year':imdb_scrape.css('span.cli-title-metadata-item::text').get(),
                 'Rating':imdb_scrape.css('span.ipc-rating-star--rating::text').get() 
            }

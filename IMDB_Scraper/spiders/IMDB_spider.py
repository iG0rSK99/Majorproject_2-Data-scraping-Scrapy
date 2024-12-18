import scrapy
import json
from IMDB_Scraper.items import info

class ImdbSpiderSpider(scrapy.Spider):
    name = "IMDB_spider"
    allowed_domains = ["imbd.com"]
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        raw_data=response.css("script[id='__NEXT_DATA__']::text").get()
        json_data= json.loads(raw_data)
        needed_data= json_data['props']['pageProps']['pageData']['chartTitles']['edges']
        
        information= info()
        for movie in needed_data:

            information['title'] = movie['node']['titleText']['text'],
            information['release_year'] = movie['node']['releaseYear']['year'],
            information['rating'] = movie['node']['ratingsSummary']['aggregateRating']

            yield information

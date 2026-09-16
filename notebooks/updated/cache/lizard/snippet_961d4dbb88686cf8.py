def rss_parse(self, response):
    for item in response.xpath('//item'):
        for url in item.xpath('link/text()').extract():
            yield scrapy.Request(url, lambda resp: self.article_parse(resp,
                item.xpath('title/text()').extract()[0]))
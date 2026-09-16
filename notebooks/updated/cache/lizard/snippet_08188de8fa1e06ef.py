def article_parse(self, response, rss_title=None):
    if not self.helper.parse_crawler.content_type(response):
        return
    yield self.helper.parse_crawler.pass_to_pipeline_if_article(response,
        self.ignored_allowed_domain, self.original_url, rss_title)
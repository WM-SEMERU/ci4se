def load_from_config(self, config):
    self.site = config.get('id', False)
    self.uri_base = config.get('uri_base', False)
    self.uris_to_crawl = self.crawlpage.get_uris(base_uri=self.uri_base,
        filter_list=config.get('crawl_uri_filters', None))
    self.is_consume_page = self.crawlpage.has_selector(config.get(
        'consume_selector', False))
def setup_rabbitmq(self):
    if not self.rabbitmq_key:
        self.rabbitmq_key = '{}:start_urls'.format(self.name)
    self.server = connection.from_settings(self.crawler.settings)
    self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
    self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped
        )
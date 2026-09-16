def get_spider_stats(self, spider_name):
    if spider_name is None:
        spider_name = self.spider_name
    else:
        self.spider_name = spider_name
    if self.spider_name is None:
        self.spider_name = self.list_running()[0].split(':')[-1]
    return self.jsonrpc_call('stats', 'get_stats', self.spider_name)
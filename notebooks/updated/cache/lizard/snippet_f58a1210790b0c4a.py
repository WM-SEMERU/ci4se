def open_spider(self, spider):
    if self.url == '':
        self.client = pymongo.MongoClient(self.host, self.port)
    else:
        self.client = pymongo.MongoClient(self.url)
    self.db_name, self.collection_name = self._replace_placeholder(spider)
    self.db = self.client[self.db_name]
def get_item(self, url):
    _hash = self.build_hash(url)
    query = {'_id': _hash}
    return self.dbase.cache.find_one(query)
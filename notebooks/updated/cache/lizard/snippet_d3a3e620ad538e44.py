def set_item(self, key, url):
    if self._db.search(self._urls.key == key):
        self._db.update({'url': url}, self._urls.key == key)
    else:
        self._db.insert({'key': key, 'url': url})
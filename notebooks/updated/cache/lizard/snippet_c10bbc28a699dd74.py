def load(self, response):
    if 'href' in response:
        self._href = response.pop('href')
    if self.data_key and self.data_key in response:
        self._data.update(response.pop(self.data_key))
        for rel in [x for x in self.relationships if x in response and
            response[x]]:
            rel_class = self.relationships[rel]
            collection = rel_class.collection_class(self.client, rel_class,
                parent=self)
            self._relationship_cache[rel] = collection(response[rel])
    else:
        self._data.update(response)
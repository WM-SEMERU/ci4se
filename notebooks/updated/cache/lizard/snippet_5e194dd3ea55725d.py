def register(self, correlation_id, key, connection):
    item = DiscoveryItem()
    item.key = key
    item.connection = connection
    self._items.append(item)
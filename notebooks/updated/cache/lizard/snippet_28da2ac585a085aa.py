async def get(self, key):
    log.info('Looking up key %s', key)
    dkey = digest(key)
    if self.storage.get(dkey) is not None:
        return self.storage.get(dkey)
    node = Node(dkey)
    nearest = self.protocol.router.find_neighbors(node)
    if not nearest:
        log.warning('There are no known neighbors to get key %s', key)
        return None
    spider = ValueSpiderCrawl(self.protocol, node, nearest, self.ksize,
        self.alpha)
    return await spider.find()
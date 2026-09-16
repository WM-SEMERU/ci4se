def clear(self, only_read=False):
    self.cache_items.clear()
    self.total_access_count = 0
    self.logger.debug('Cache clear operation is completed')
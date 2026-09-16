def get_pks_for_filter(self, key, filter_type, value):
    start, end, __ = self.get_boundaries(filter_type, value)
    return self.connection.zrangebyscore(key, start, end)
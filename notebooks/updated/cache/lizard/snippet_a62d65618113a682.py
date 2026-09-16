def between(self, min, max, limit=None, offset=None):
    if limit is not None and offset is None:
        offset = 0
    return self.zrangebyscore(min, max, start=offset, num=limit)
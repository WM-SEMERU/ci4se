def exists(self):
    limit = self.limit_
    result = self.limit(1).count() > 0
    self.limit(limit)
    return result
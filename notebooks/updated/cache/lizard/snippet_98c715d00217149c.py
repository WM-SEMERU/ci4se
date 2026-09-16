def intersect(self, other):
    return DataFrame(self._jdf.intersect(other._jdf), self.sql_ctx)
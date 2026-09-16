def dropDuplicates(self, subset=None):
    if subset is None:
        jdf = self._jdf.dropDuplicates()
    else:
        jdf = self._jdf.dropDuplicates(self._jseq(subset))
    return DataFrame(jdf, self.sql_ctx)
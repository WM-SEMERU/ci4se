def imap_unordered_async(self, func, iterable, chunksize=None, callback=None):
    apply_result = ApplyResult(callback=callback)
    collector = UnorderedResultCollector(apply_result)
    self._create_sequences(func, iterable, chunksize, collector)
    return apply_result
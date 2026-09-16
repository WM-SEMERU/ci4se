def _fill_result_cache(self):
    idx = 0
    try:
        while True:
            idx += 1000
            self._fill_result_cache_to_idx(idx)
    except StopIteration:
        pass
    self._count = len(self._result_cache)
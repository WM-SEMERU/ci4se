def fetch_next_block(self):
    results = []
    for _ in xrange(self._page_size):
        try:
            results.append(next(self))
        except StopIteration:
            break
    return results
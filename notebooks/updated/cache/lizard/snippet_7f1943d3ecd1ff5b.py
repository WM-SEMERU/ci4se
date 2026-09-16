def sample(self, cursor):
    count = cursor.count()
    if count == 0:
        self._empty = True
        raise ValueError('Empty collection')
    if self.p >= 1 and self.max_items <= 0:
        for item in cursor:
            yield item
        return
    if self.max_items <= 0:
        n_target = max(self.min_items, self.p * count)
    elif self.p <= 0:
        n_target = max(self.min_items, self.max_items)
    else:
        n_target = max(self.min_items, min(self.max_items, self.p * count))
    if n_target == 0:
        raise ValueError('No items requested')
    n = 0
    while n < n_target:
        try:
            item = next(cursor)
        except StopIteration:
            cursor.rewind()
            item = next(cursor)
        if self._keep():
            yield item
            n += 1
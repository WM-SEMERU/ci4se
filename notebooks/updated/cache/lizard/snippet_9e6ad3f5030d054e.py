def _split(self, rect):
    max_rects = collections.deque()
    for r in self._max_rects:
        if r.intersects(rect):
            max_rects.extend(self._generate_splits(r, rect))
        else:
            max_rects.append(r)
    self._max_rects = list(max_rects)
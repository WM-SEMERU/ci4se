def distribution(self, start=None, end=None, normalized=True, mask=None):
    start, end, mask = self._check_boundaries(start, end, mask=mask)
    counter = histogram.Histogram()
    for start, end, _ in mask.iterperiods(value=True):
        for t0, t1, value in self.iterperiods(start, end):
            duration = utils.duration_to_number(t1 - t0, units='seconds')
            try:
                counter[value] += duration
            except histogram.UnorderableElements as e:
                counter = histogram.Histogram.from_dict(dict(counter), key=hash
                    )
                counter[value] += duration
    if normalized:
        return counter.normalized()
    else:
        return counter
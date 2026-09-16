def coverageCounts(self):
    coverageCounts = Counter()
    for start, end in self._intervals:
        coverageCounts.update(range(max(0, start), min(self._targetLength,
            end)))
    return coverageCounts
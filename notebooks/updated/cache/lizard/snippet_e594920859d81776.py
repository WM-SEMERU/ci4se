def increment_bucket_count(self, value):
    if len(self._bounds) == 0:
        self._counts_per_bucket[0] += 1
        return 0
    for ii, bb in enumerate(self._bounds):
        if value < bb:
            self._counts_per_bucket[ii] += 1
            return ii
    else:
        last_bucket_index = len(self._bounds)
        self._counts_per_bucket[last_bucket_index] += 1
        return last_bucket_index
def update(self, other):

    def update_sortedset_trans(pipe):
        items = other._data(pipe=pipe) if use_redis else other._data()
        pipe.multi()
        for member, score in items:
            pipe.zadd(self.key, {self._pickle(member): float(score)})

    def update_mapping_trans(pipe):
        items = other.items(pipe=pipe) if use_redis else other.items()
        pipe.multi()
        for place, value in items:
            self.set_location(place, value['latitude'], value['longitude'],
                pipe=pipe)

    def update_tuples_trans(pipe):
        items = other.__iter__(pipe=pipe) if use_redis else other.__iter__()
        pipe.multi()
        for place, latitude, longitude in items:
            self.set_location(place, latitude, longitude, pipe=pipe)
    watches = []
    if self._same_redis(other, RedisCollection):
        use_redis = True
        watches.append(other.key)
    else:
        use_redis = False
    if isinstance(other, SortedSetBase):
        func = update_sortedset_trans
    elif hasattr(other, 'items'):
        func = update_mapping_trans
    elif hasattr(other, '__iter__'):
        func = update_tuples_trans
    self._transaction(func, *watches)
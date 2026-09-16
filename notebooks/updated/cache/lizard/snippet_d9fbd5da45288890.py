def get_locations(self, locations, as_list=False):
    indexes = [self._index[x] for x in locations]
    return self.get(indexes, as_list)
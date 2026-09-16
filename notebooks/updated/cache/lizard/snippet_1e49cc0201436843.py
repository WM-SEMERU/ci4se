def aggregate_by_index(self, function, level=0):
    result = self._map_by_index(function, level=level)
    return result.map(lambda v: array(v), index=result.index)
def mean(self):
    _self = self._discard_value(None)
    if not _self.total():
        return None
    weighted_sum = sum(key * value for key, value in iteritems(_self))
    return weighted_sum / float(_self.total())
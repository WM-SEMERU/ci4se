def search_range(self, value):
    if value == 0 or not value % 16:
        self._search_range = value
    else:
        raise InvalidSearchRangeError('Search range must be a multiple of 16.')
    self._replace_bm()
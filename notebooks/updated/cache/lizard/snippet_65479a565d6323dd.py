def set_max_beds(self, max_beds):
    if not isinstance(max_beds, int):
        raise DaftException('Maximum number of beds should be an integer.')
    self._max_beds = str(max_beds)
    self._query_params += str(QueryParam.MAX_BEDS) + self._max_beds
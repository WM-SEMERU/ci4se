def get_data_raw(self, request):
    path = '/api/1.0/data/raw/'
    res = self._api_post(definition.RawDataResponse, path, request)
    token = res.continuation_token
    while token is not None:
        res2 = self.get_data_raw_with_token(token)
        res.series += res2.series
        token = res2.continuation_token
    return res
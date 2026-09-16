def _get_datapoints(self, params):
    url = self.query_uri + '/v1/datapoints'
    return self.service._get(url, params=params)
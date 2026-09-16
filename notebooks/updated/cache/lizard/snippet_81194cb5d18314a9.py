def get_single_series(self, id):
    url = '%s/%s' % (Series.resource_url(), id)
    response = json.loads(self._call(url).text)
    return SeriesDataWrapper(self, response)
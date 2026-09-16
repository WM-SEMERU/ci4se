def get_series_by_name(self, series_name):
    try:
        return self.api.search_series(name=series_name), None
    except exceptions.TVDBRequestException as err:
        LOG.exception('search for series %s failed', series_name)
        return None, _as_str(err)
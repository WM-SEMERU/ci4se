def get_series_vintage_dates(self, series_id):
    url = '%s/series/vintagedates?series_id=%s' % (self.root_url, series_id)
    root = self.__fetch_data(url)
    if root is None:
        raise ValueError('No vintage date exists for series id: ' + series_id)
    dates = []
    for child in root.getchildren():
        dates.append(self._parse(child.text))
    return dates
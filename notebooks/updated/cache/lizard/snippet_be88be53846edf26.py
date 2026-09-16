def add_data_set(self, data, series_type='map', name=None, is_coordinate=
    False, **kwargs):
    self.data_set_count += 1
    if not name:
        name = 'Series %d' % self.data_set_count
    kwargs.update({'name': name})
    if is_coordinate:
        self.data_is_coordinate = True
        self.add_JSsource(
            'https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.3.6/proj4.js')
        if self.map and not self.data_temp:
            series_data = Series([], series_type='map', **{'mapData': self.map}
                )
            series_data.__options__().update(SeriesOptions(series_type=
                'map', **{'mapData': self.map}).__options__())
            self.data_temp.append(series_data)
    if self.map and 'mapData' in kwargs.keys():
        kwargs.update({'mapData': self.map})
    series_data = Series(data, series_type=series_type, **kwargs)
    series_data.__options__().update(SeriesOptions(series_type=series_type,
        **kwargs).__options__())
    self.data_temp.append(series_data)
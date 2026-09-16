def add_series(self, name, number_format=None):
    series_data = BubbleSeriesData(self, name, number_format)
    self.append(series_data)
    return series_data
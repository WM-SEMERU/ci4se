def number_format(self):
    number_format = self._number_format
    if number_format is None:
        return self._series_data.number_format
    return number_format
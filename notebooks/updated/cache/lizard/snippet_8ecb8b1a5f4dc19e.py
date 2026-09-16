def year(self, value=None):
    if value is not None:
        try:
            value = int(value)
        except ValueError:
            raise ValueError('value {} need to be of type int for field `year`'
                .format(value))
    self._year = value
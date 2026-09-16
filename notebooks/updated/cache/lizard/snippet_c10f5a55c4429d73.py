def _convert_value(self, item):
    if item.ctype == 3:
        try:
            return datetime.datetime(*xlrd.xldate_as_tuple(item.value, self
                ._book.datemode))
        except ValueError:
            return item.value
    if item.ctype == 2:
        if item.value % 1 == 0:
            return int(item.value)
        else:
            return item.value
    return item.value
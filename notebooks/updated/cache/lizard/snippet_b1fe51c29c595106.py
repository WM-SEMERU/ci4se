def _number_of_rows(self, start=0, count=100, **kwargs):
    first = str(start)
    last = str(start + count)
    string_format = ':'.join([first, last])
    return string_format
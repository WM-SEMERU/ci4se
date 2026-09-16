def value_from_datadict(self, data, files, name):
    y = data.get(self.year_field % name)
    m = data.get(self.month_field % name)
    d = data.get(self.day_field % name)
    if y == 'YYYY':
        y = ''
    if m == 'MM':
        m = ''
    if d == 'DD':
        d = ''
    date = y
    if m:
        date += '-%s' % m
        if d:
            date += '-%s' % d
    return date
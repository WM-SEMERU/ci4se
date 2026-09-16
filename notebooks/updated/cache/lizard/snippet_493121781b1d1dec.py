def from_json(cls, data):
    if 'month' not in data:
        data['month'] = 1
    if 'day' not in data:
        data['day'] = 1
    if 'hour' not in data:
        data['hour'] = 0
    if 'minute' not in data:
        data['minute'] = 0
    if 'year' not in data:
        data['year'] = 2017
    leap_year = True if int(data['year']) == 2016 else False
    return cls(data['month'], data['day'], data['hour'], data['minute'],
        leap_year)
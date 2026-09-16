def get_daily(self, date=None):
    if date == None:
        return self.get('/daily.json')
    url = '/daily/{}/{}/{}.json'.format(date.year, date.month, date.day)
    return self.get(url)
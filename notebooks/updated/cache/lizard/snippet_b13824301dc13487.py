def minutes(self, start_date=None, end_date=None, grouping=None):
    data = self.__format(start_date, end_date)
    url = self.base_url + '/minutes'
    return self.get(url, data=data)
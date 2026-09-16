def month(self):
    url = '/stats/month'
    result = self._get(url)
    return StatModel.parse(result)
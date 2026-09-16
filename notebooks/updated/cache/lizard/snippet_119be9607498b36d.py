def info(self):
    url = '{}/v7/finance/quote?symbols={}'.format(self._base_url, self.ticker)
    r = _requests.get(url=url).json()['quoteResponse']['result']
    if len(r) > 0:
        return r[0]
    return {}
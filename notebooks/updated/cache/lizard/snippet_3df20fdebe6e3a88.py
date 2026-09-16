def count(self, eventRegistry):
    self.setRequestedResult(RequestEventArticles(**self.queryParams))
    res = eventRegistry.execQuery(self)
    if 'error' in res:
        print(res['error'])
    count = res.get(self.queryParams['eventUri'], {}).get('articles', {}).get(
        'totalResults', 0)
    return count
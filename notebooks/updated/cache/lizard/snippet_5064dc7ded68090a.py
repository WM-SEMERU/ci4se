def iter(self):
    page = 1
    fetch_all = True
    url = '{}/{}'.format(__endpoint__, self.type.RESOURCE)
    if 'page' in self.params:
        page = self.params['page']
        fetch_all = False
    response = RestClient.get(url, self.params)[self.type.RESOURCE]
    while len(response):
        for item in response:
            yield self.type(item)
        if not fetch_all:
            break
        else:
            page += 1
            self.where(page=page)
        response = RestClient.get(url, self.params)[self.type.RESOURCE]
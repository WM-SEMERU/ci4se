def crawl(self, urls, name='crawl', api='analyze', **kwargs):
    if isinstance(urls, list):
        urls = ' '.join(urls)
    url = self.endpoint('crawl')
    process_url = self.endpoint(api)
    params = {'token': self._token, 'seeds': urls, 'name': name, 'apiUrl':
        process_url}
    params['maxToCrawl'] = 10
    params.update(kwargs)
    self._get(url, params=params)
    return Job(self._token, name, self._version)
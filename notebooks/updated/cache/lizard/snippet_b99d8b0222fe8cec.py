def search(self, query, pagination, result_field):
    result = []
    url = '/'.join((self.url, query))
    while url:
        log.debug('Pagure query: {0}'.format(url))
        try:
            response = requests.get(url, headers=self.headers)
            log.data('Response headers:\n{0}'.format(response.headers))
        except requests.RequestException as error:
            log.error(error)
            raise ReportError('Pagure search {0} failed.'.format(self.url))
        data = response.json()
        objects = data[result_field]
        log.debug('Result: {0} fetched'.format(listed(len(objects), 'item')))
        log.data(pretty(data))
        if not objects:
            break
        result.extend(objects)
        url = data[pagination]['next']
    return result
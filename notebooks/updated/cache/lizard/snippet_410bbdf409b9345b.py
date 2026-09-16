def getNodes(self, networkId, column, query, verbose=None):
    response = api(url=self.___url + 'networks/' + str(networkId) +
        '/nodes', PARAMS={'column': column, 'query': query}, method='GET',
        verbose=verbose, parse_params=False)
    return response
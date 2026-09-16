def updateTable(self, networkId, tableType, body, class_, verbose=None):
    response = api(url=self.___url + 'networks/' + str(networkId) +
        '/tables/' + str(tableType) + '', method='PUT', body=body, verbose=
        verbose)
    return response
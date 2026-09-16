def applyStyle(self, styleName, networkId, verbose=None):
    response = api(url=self.___url + 'apply/styles/' + str(styleName) + '/' +
        str(networkId) + '', method='GET', verbose=verbose, parse_params=False)
    return response
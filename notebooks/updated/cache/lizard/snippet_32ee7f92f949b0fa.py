def getStyleCount(self, verbose=None):
    response = api(url=self.___url + 'styles/count', method='GET', verbose=
        verbose, parse_params=False)
    return response
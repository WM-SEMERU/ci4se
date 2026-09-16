def filing_history(self, num, transaction=None, **kwargs):
    baseuri = self._BASE_URI + 'company/{}/filing-history'.format(num)
    if transaction is not None:
        baseuri += '/{}'.format(transaction)
    res = self.session.get(baseuri, params=kwargs)
    self.handle_http_error(res)
    return res
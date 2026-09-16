def create_account(self, currency=None):
    url = '{0}/{1}/accounts'.format(self.domain, self.API_VERSION)
    params = {'currency': currency}
    try:
        return self._Client__call(uri=url, params=params, method='post')
    except RequestException:
        return False
    except AssertionError:
        return False
def get_authorize_url(self, **params):
    params.update({'client_id': self.client_id})
    return self.authorize_url + '?' + urlencode(params)
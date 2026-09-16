def get_capacity(self, legacy=None):
    params = None
    if legacy:
        params = {'legacy': legacy}
    return self.call_api('/capacity', params=params)['capacity']
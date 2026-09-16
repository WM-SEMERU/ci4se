def retry(self, index=None, params=None):
    return self.transport.perform_request('POST', _make_path(index, '_ilm',
        'retry'), params=params)
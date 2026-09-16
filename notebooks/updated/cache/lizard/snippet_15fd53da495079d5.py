def status(self, repository=None, snapshot=None, params=None):
    return self.transport.perform_request('GET', _make_path('_snapshot',
        repository, snapshot, '_status'), params=params)
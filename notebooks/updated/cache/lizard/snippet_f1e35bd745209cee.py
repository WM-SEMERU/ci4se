def has_in_starred(self, starred):
    assert isinstance(starred, github.Repository.Repository), starred
    status, headers, data = self._requester.requestJson('GET', 
        '/user/starred/' + starred._identity)
    return status == 204
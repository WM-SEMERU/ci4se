def get_keys(self):
    return github.PaginatedList.PaginatedList(github.UserKey.UserKey, self.
        _requester, self.url + '/keys', None)
def has_in_members(self, member):
    assert isinstance(member, github.NamedUser.NamedUser), member
    status, headers, data = self._requester.requestJson('GET', self.url +
        '/members/' + member._identity)
    return status == 204
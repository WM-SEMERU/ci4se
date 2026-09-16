def get_comment(self, id):
    assert isinstance(id, (int, long)), id
    headers, data = self._requester.requestJsonAndCheck('GET', self.url +
        '/comments/' + str(id))
    return github.GistComment.GistComment(self._requester, headers, data,
        completed=True)
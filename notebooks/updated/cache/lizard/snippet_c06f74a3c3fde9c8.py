def get_git_blob(self, sha):
    assert isinstance(sha, (str, unicode)), sha
    headers, data = self._requester.requestJsonAndCheck('GET', self.url +
        '/git/blobs/' + sha)
    return github.GitBlob.GitBlob(self._requester, headers, data, completed
        =True)
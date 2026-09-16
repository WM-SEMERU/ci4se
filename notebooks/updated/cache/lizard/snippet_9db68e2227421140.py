def create_gist(self, public, files, description=github.GithubObject.NotSet):
    assert isinstance(public, bool), public
    assert all(isinstance(element, github.InputFileContent) for element in
        files.itervalues()), files
    assert description is github.GithubObject.NotSet or isinstance(description,
        (str, unicode)), description
    post_parameters = {'public': public, 'files': {key: value._identity for
        key, value in files.iteritems()}}
    if description is not github.GithubObject.NotSet:
        post_parameters['description'] = description
    headers, data = self._requester.requestJsonAndCheck('POST', '/gists',
        input=post_parameters)
    return github.Gist.Gist(self._requester, headers, data, completed=True)
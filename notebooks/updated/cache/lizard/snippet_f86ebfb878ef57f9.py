def create_team(self, name, repo_names=github.GithubObject.NotSet,
    permission=github.GithubObject.NotSet, privacy=github.GithubObject.NotSet):
    assert isinstance(name, (str, unicode)), name
    assert repo_names is github.GithubObject.NotSet or all(isinstance(
        element, github.Repository.Repository) for element in repo_names
        ), repo_names
    assert permission is github.GithubObject.NotSet or isinstance(permission,
        (str, unicode)), permission
    assert privacy is github.GithubObject.NotSet or isinstance(privacy, (
        str, unicode)), privacy
    post_parameters = {'name': name}
    if repo_names is not github.GithubObject.NotSet:
        post_parameters['repo_names'] = [element._identity for element in
            repo_names]
    if permission is not github.GithubObject.NotSet:
        post_parameters['permission'] = permission
    if privacy is not github.GithubObject.NotSet:
        post_parameters['privacy'] = privacy
    headers, data = self._requester.requestJsonAndCheck('POST', self.url +
        '/teams', input=post_parameters)
    return github.Team.Team(self._requester, headers, data, completed=True)
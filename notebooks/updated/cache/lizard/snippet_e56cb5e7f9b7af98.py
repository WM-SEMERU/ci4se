def get_cards(self, archived_state=github.GithubObject.NotSet):
    assert archived_state is github.GithubObject.NotSet or isinstance(
        archived_state, (str, unicode)), archived_state
    url_parameters = dict()
    if archived_state is not github.GithubObject.NotSet:
        url_parameters['archived_state'] = archived_state
    return github.PaginatedList.PaginatedList(github.ProjectCard.
        ProjectCard, self._requester, self.url + '/cards', url_parameters,
        {'Accept': Consts.mediaTypeProjectsPreview})
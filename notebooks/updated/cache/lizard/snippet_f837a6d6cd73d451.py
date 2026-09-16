def search_users(self, query, sort=github.GithubObject.NotSet, order=github
    .GithubObject.NotSet, **qualifiers):
    assert isinstance(query, (str, unicode)), query
    url_parameters = dict()
    if sort is not github.GithubObject.NotSet:
        assert sort in ('followers', 'repositories', 'joined'), sort
        url_parameters['sort'] = sort
    if order is not github.GithubObject.NotSet:
        assert order in ('asc', 'desc'), order
        url_parameters['order'] = order
    query_chunks = []
    if query:
        query_chunks.append(query)
    for qualifier, value in qualifiers.items():
        query_chunks.append('%s:%s' % (qualifier, value))
    url_parameters['q'] = ' '.join(query_chunks)
    assert url_parameters['q'], 'need at least one qualifier'
    return github.PaginatedList.PaginatedList(github.NamedUser.NamedUser,
        self.__requester, '/search/users', url_parameters)
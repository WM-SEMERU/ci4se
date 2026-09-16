def push(self, repository, tag=None, stream=False, auth_config=None, decode
    =False):
    if not tag:
        repository, tag = utils.parse_repository_tag(repository)
    registry, repo_name = auth.resolve_repository_name(repository)
    u = self._url('/images/{0}/push', repository)
    params = {'tag': tag}
    headers = {}
    if auth_config is None:
        header = auth.get_config_header(self, registry)
        if header:
            headers['X-Registry-Auth'] = header
    else:
        log.debug('Sending supplied auth config')
        headers['X-Registry-Auth'] = auth.encode_header(auth_config)
    response = self._post_json(u, None, headers=headers, stream=stream,
        params=params)
    self._raise_for_status(response)
    if stream:
        return self._stream_helper(response, decode=decode)
    return self._result(response)
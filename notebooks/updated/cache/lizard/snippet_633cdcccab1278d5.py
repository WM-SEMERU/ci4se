def recent(self, username, project, limit=1, offset=0, branch=None,
    status_filter=''):
    method = 'GET'
    if branch is not None:
        url = (
            '/project/{username}/{project}/tree/{branch}?circle-token={token}&limit={limit}&offset={offset}&filter={status_filter}'
            .format(username=username, project=project, branch=branch,
            token=self.client.api_token, limit=limit, offset=offset,
            status_filter=status_filter))
    else:
        url = (
            '/project/{username}/{project}?circle-token={token}&limit={limit}&offset={offset}&filter={status_filter}'
            .format(username=username, project=project, token=self.client.
            api_token, limit=limit, offset=offset, status_filter=status_filter)
            )
    json_data = self.client.request(method, url)
    return json_data
def repo_list(self, project_key, start=None, limit=25):
    url = 'rest/api/1.0/projects/{projectKey}/repos'.format(projectKey=
        project_key)
    params = {}
    if limit:
        params['limit'] = limit
    if start:
        params['start'] = start
    response = self.get(url, params=params)
    if response.get('isLastPage'):
        log.info('This is a last page of the result')
    else:
        log.info('Next page start at {}'.format(response.get('nextPageStart')))
    return (response or {}).get('values')
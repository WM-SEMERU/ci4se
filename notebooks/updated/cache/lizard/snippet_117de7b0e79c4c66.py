def my_permissions(self, projectKey=None, projectId=None, issueKey=None,
    issueId=None):
    params = {}
    if projectKey is not None:
        params['projectKey'] = projectKey
    if projectId is not None:
        params['projectId'] = projectId
    if issueKey is not None:
        params['issueKey'] = issueKey
    if issueId is not None:
        params['issueId'] = issueId
    return self._get_json('mypermissions', params=params)
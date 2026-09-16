def patch_resource(self, path, body=None, json=None):
    url = '%s%s' % (path, self._param_list())
    headers = {'Accept': 'application/json;odata=minimalmetadata'}
    if json:
        headers['Content-Type'] = 'application/json'
        body = json_dumps(json)
    response = O365_DAO().patchURL(self._url(url), headers, body)
    if not (response.status == 200 or response.status == 201 or response.
        status == 204):
        raise DataFailureException(url, response.status, response.data)
    return json_loads(response.data) if len(response.data) else {}
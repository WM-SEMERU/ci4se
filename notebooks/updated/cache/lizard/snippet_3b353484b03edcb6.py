def _make_request(self, api_resource, method='GET', params=None, **kwargs):
    if kwargs.get('json'):
        headers = {'Authorization': 'Bearer {}'.format(self._token),
            'Content-Type': 'application/json'}
    else:
        headers = {'Authorization': 'Bearer {}'.format(self._token)}
    response = requests.request(method=method, url='{0}{1}'.format(self.
        BASE_API_URL, api_resource), headers=headers, params=params, **kwargs)
    if response.status_code >= 400:
        error_response = response.json()
        raise ToshlException(status_code=response.status_code, error_id=
            error_response['error_id'], error_description=error_response[
            'description'], extra_info=error_response.get('fields'))
    return response
def update_resource(self, path, data, if_match=None):
    response = self._http_request(resource=path, method='PUT', body=data,
        if_match=if_match)
    try:
        return response.json()
    except ValueError:
        raise exception.ServiceException('Invalid service response.')
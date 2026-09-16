def delete_endpoint(self, endpoint_id):
    self._validate_uuid(endpoint_id)
    url = '/notification/v1/endpoint/{}'.format(endpoint_id)
    response = NWS_DAO().deleteURL(url, self._write_headers())
    if response.status != 204:
        raise DataFailureException(url, response.status, response.data)
    return response.status
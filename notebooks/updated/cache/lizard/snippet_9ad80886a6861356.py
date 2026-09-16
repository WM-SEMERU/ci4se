def exists(self, **kwargs):
    requests_params = self._handle_requests_params(kwargs)
    self._check_load_parameters(**kwargs)
    kwargs['uri_as_parts'] = True
    session = self._meta_data['bigip']._meta_data['icr_session']
    base_uri = self._meta_data['container']._meta_data['uri']
    kwargs.update(requests_params)
    try:
        response = session.get(base_uri, **kwargs)
    except HTTPError as err:
        if err.response.status_code == 404:
            return False
        else:
            raise
    rdict = response.json()
    if 'address' not in rdict:
        return False
    return True
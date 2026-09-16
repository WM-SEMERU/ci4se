def _prepare_put_or_patch(self, kwargs):
    requests_params = self._handle_requests_params(kwargs)
    update_uri = self._meta_data['uri']
    session = self._meta_data['bigip']._meta_data['icr_session']
    read_only = self._meta_data.get('read_only_attributes', [])
    return requests_params, update_uri, session, read_only
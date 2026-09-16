def get_metadata(self, dataset_identifier, content_type='json'):
    resource = _format_old_api_request(dataid=dataset_identifier,
        content_type=content_type)
    return self._perform_request('get', resource)
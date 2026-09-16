def create_file(self, share_name, directory_name, file_name, content_length,
    content_settings=None, metadata=None, timeout=None):
    _validate_not_none('share_name', share_name)
    _validate_not_none('file_name', file_name)
    _validate_not_none('content_length', content_length)
    request = HTTPRequest()
    request.method = 'PUT'
    request.host_locations = self._get_host_locations()
    request.path = _get_path(share_name, directory_name, file_name)
    request.query = {'timeout': _int_to_str(timeout)}
    request.headers = {'x-ms-content-length': _to_str(content_length),
        'x-ms-type': 'file'}
    _add_metadata_headers(metadata, request)
    if content_settings is not None:
        request.headers.update(content_settings._to_headers())
    self._perform_request(request)
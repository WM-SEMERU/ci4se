def abort_copy_file(self, share_name, directory_name, file_name, copy_id,
    timeout=None):
    _validate_not_none('share_name', share_name)
    _validate_not_none('file_name', file_name)
    _validate_not_none('copy_id', copy_id)
    request = HTTPRequest()
    request.method = 'PUT'
    request.host_locations = self._get_host_locations()
    request.path = _get_path(share_name, directory_name, file_name)
    request.query = {'comp': 'copy', 'copyid': _to_str(copy_id), 'timeout':
        _int_to_str(timeout)}
    request.headers = {'x-ms-copy-action': 'abort'}
    self._perform_request(request)
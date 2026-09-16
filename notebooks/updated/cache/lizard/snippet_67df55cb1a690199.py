def get_directory_properties(self, share_name, directory_name, timeout=None,
    snapshot=None):
    _validate_not_none('share_name', share_name)
    _validate_not_none('directory_name', directory_name)
    request = HTTPRequest()
    request.method = 'GET'
    request.host_locations = self._get_host_locations()
    request.path = _get_path(share_name, directory_name)
    request.query = {'restype': 'directory', 'timeout': _int_to_str(timeout
        ), 'sharesnapshot': _to_str(snapshot)}
    return self._perform_request(request, _parse_directory, [directory_name])
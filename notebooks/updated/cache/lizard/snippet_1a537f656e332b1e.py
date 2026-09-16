def delete_share(self, share_name, fail_not_exist=False, timeout=None,
    snapshot=None, delete_snapshots=None):
    _validate_not_none('share_name', share_name)
    request = HTTPRequest()
    request.method = 'DELETE'
    request.host_locations = self._get_host_locations()
    request.path = _get_path(share_name)
    request.headers = {'x-ms-delete-snapshots': _to_str(delete_snapshots)}
    request.query = {'restype': 'share', 'timeout': _int_to_str(timeout),
        'sharesnapshot': _to_str(snapshot)}
    if not fail_not_exist:
        try:
            self._perform_request(request, expected_errors=[
                _SHARE_NOT_FOUND_ERROR_CODE])
            return True
        except AzureHttpError as ex:
            _dont_fail_not_exist(ex)
            return False
    else:
        self._perform_request(request)
        return True
def delete_table(self, table_name, fail_not_exist=False, timeout=None):
    _validate_not_none('table_name', table_name)
    request = HTTPRequest()
    request.method = 'DELETE'
    request.host_locations = self._get_host_locations()
    request.path = "/Tables('" + _to_str(table_name) + "')"
    request.query = {'timeout': _int_to_str(timeout)}
    request.headers = {_DEFAULT_ACCEPT_HEADER[0]: _DEFAULT_ACCEPT_HEADER[1]}
    if not fail_not_exist:
        try:
            self._perform_request(request)
            return True
        except AzureHttpError as ex:
            _dont_fail_not_exist(ex)
            return False
    else:
        self._perform_request(request)
        return True
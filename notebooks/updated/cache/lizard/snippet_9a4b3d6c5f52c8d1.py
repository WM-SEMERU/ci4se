def set_table_acl(self, table_name, signed_identifiers=None, timeout=None):
    _validate_not_none('table_name', table_name)
    _validate_access_policies(signed_identifiers)
    request = HTTPRequest()
    request.method = 'PUT'
    request.host_locations = self._get_host_locations()
    request.path = '/' + _to_str(table_name)
    request.query = {'comp': 'acl', 'timeout': _int_to_str(timeout)}
    request.body = _get_request_body(_convert_signed_identifiers_to_xml(
        signed_identifiers))
    self._perform_request(request)
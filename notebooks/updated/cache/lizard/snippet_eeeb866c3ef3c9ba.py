def _list_queues(self, prefix=None, marker=None, max_results=None, include=
    None, timeout=None):
    request = HTTPRequest()
    request.method = 'GET'
    request.host = self._get_host()
    request.path = _get_path()
    request.query = [('comp', 'list'), ('prefix', _to_str(prefix)), (
        'marker', _to_str(marker)), ('maxresults', _int_to_str(max_results)
        ), ('include', _to_str(include)), ('timeout', _int_to_str(timeout))]
    response = self._perform_request(request)
    return _convert_xml_to_queues(response)
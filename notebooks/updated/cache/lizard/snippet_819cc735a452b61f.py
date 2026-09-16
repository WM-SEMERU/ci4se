def GET_namespaces(self, path_info):
    qs_values = path_info['qs_values']
    offset = qs_values.get('offset', None)
    count = qs_values.get('count', None)
    blockstackd_url = get_blockstackd_url()
    namespaces = blockstackd_client.get_all_namespaces(offset=offset, count
        =count, hostport=blockstackd_url)
    if json_is_error(namespaces):
        status_code = namespaces.get('http_status', 502)
        return self._reply_json({'error': namespaces['error']}, status_code
            =status_code)
    self._reply_json(namespaces)
    return
def _query(api_version=None, data=None):
    if data is None:
        data = {}
    ret = {'res': True}
    api_url = 'https://api.random.org/'
    base_url = _urljoin(api_url, 'json-rpc/' + six.text_type(api_version) +
        '/invoke')
    data = salt.utils.json.dumps(data)
    result = salt.utils.http.query(base_url, method='POST', params={}, data
        =data, decode=True, status=True, header_dict={}, opts=__opts__)
    if result.get('status', None) == salt.ext.six.moves.http_client.OK:
        _result = result['dict']
        if _result.get('result'):
            return _result.get('result')
        if _result.get('error'):
            return _result.get('error')
        return False
    elif result.get('status', None
        ) == salt.ext.six.moves.http_client.NO_CONTENT:
        return False
    else:
        ret['message'] = result.text if hasattr(result, 'text') else ''
        return ret
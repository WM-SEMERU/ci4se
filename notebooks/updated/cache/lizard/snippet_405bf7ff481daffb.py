def api_request(api_base_url='http://localhost:8080/', path='', method=
    'get', data=None, params={}, verify=True, cert=list()):
    method = method.lower()
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'
        }
    methods = {'get': requests.get, 'post': requests.post}
    if path[0] != '/':
        path = '/{0}'.format(path)
    if params:
        path += '?{0}'.format(urllib.urlencode(params))
    url = '{0}{1}'.format(api_base_url, path)
    resp = methods[method](url, data=json.dumps(data), headers=headers,
        verify=verify, cert=cert)
    return resp
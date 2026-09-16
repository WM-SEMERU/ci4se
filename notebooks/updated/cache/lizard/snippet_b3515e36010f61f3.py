def _call_method(self, method, req, resp_class):
    payload = req.SerializeToString()
    headers = {'Content-Type': 'application/x-protobuf', 'Content-Length':
        str(len(payload)), 'X-Goog-Api-Format-Version': '2'}
    response, content = self._http.request('%s:%s' % (self._url, method),
        method='POST', body=payload, headers=headers)
    if response.status != 200:
        raise _make_rpc_error(method, response, content)
    resp = resp_class()
    resp.ParseFromString(content)
    return resp
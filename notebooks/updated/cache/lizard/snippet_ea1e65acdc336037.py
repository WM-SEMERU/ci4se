def partial_update(self, index, doc_type, id, doc=None, script=None, params
    =None, upsert=None, querystring_args=None):
    if querystring_args is None:
        querystring_args = {}
    if doc is None and script is None:
        raise InvalidQuery('script or doc can not both be None')
    if doc is None:
        cmd = {'script': script}
        if params:
            cmd['params'] = params
        if upsert:
            cmd['upsert'] = upsert
    else:
        cmd = {'doc': doc}
    path = make_path(index, doc_type, id, '_update')
    return self._send_request('POST', path, cmd, querystring_args)
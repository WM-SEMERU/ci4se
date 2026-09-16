def mediatype_create(name, mediatype, **kwargs):
    conn_args = _login(**kwargs)
    ret = {}
    try:
        if conn_args:
            method = 'mediatype.create'
            params = {'description': name}
            params['type'] = mediatype
            params = _params_extend(params, _ignore_name=True, **kwargs)
            ret = _query(method, params, conn_args['url'], conn_args['auth'])
            return ret['result']['mediatypeid']
        else:
            raise KeyError
    except KeyError:
        return ret
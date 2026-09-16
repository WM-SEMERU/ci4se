def user_deletemedia(mediaids, **kwargs):
    conn_args = _login(**kwargs)
    ret = {}
    try:
        if conn_args:
            method = 'user.deletemedia'
            if not isinstance(mediaids, list):
                mediaids = [mediaids]
            params = mediaids
            ret = _query(method, params, conn_args['url'], conn_args['auth'])
            return ret['result']['mediaids']
        else:
            raise KeyError
    except KeyError:
        return ret
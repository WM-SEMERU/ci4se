def mk_token(opts, tdata):
    redis_client = _redis_client(opts)
    if not redis_client:
        return {}
    hash_type = getattr(hashlib, opts.get('hash_type', 'md5'))
    tok = six.text_type(hash_type(os.urandom(512)).hexdigest())
    try:
        while redis_client.get(tok) is not None:
            tok = six.text_type(hash_type(os.urandom(512)).hexdigest())
    except Exception as err:
        log.warning(
            'Authentication failure: cannot get token %s from redis: %s',
            tok, err)
        return {}
    tdata['token'] = tok
    serial = salt.payload.Serial(opts)
    try:
        redis_client.set(tok, serial.dumps(tdata))
    except Exception as err:
        log.warning('Authentication failure: cannot save token %s to redis: %s'
            , tok, err)
        return {}
    return tdata
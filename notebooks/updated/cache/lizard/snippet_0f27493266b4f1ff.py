def _hash_internal(method, salt, password):
    if method == 'plain':
        return password, method
    if isinstance(password, text_type):
        password = password.encode('utf-8')
    if method.startswith('pbkdf2:'):
        args = method[7:].split(':')
        if len(args) not in (1, 2):
            raise ValueError('Invalid number of arguments for PBKDF2')
        method = args.pop(0)
        iterations = args and int(args[0] or 0) or DEFAULT_PBKDF2_ITERATIONS
        is_pbkdf2 = True
        actual_method = 'pbkdf2:%s:%d' % (method, iterations)
    else:
        is_pbkdf2 = False
        actual_method = method
    hash_func = _hash_funcs.get(method)
    if hash_func is None:
        raise TypeError('invalid method %r' % method)
    if is_pbkdf2:
        if not salt:
            raise ValueError('Salt is required for PBKDF2')
        rv = pbkdf2_hex(password, salt, iterations, hashfunc=hash_func)
    elif salt:
        if isinstance(salt, text_type):
            salt = salt.encode('utf-8')
        rv = hmac.HMAC(salt, password, hash_func).hexdigest()
    else:
        h = hash_func()
        h.update(password)
        rv = h.hexdigest()
    return rv, actual_method
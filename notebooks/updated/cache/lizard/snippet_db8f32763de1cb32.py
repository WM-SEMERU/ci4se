def after_init_apps(sender):
    from uliweb import settings
    from uliweb.utils.common import log
    check = settings.get_var('REDIS/check_version')
    if check:
        client = get_redis()
        try:
            info = client.info()
        except Exception as e:
            log.exception(e)
            log.error('Redis is not started!')
            return
        redis_version = info['redis_version']
        version = tuple(map(int, redis_version.split('.')))
        op = re_compare_op.search(check)
        if op:
            _op = op.group()
            _v = check[op.end() + 1:].strip()
        else:
            _op = '='
            _v = check
        nv = tuple(map(int, _v.split('.')))
        if _op == '=':
            flag = version[:len(nv)] == nv
        elif _op == '>=':
            flag = version >= nv
        elif _op == '>':
            flag = version > nv
        elif _op == '<=':
            flag = version <= nv
        elif _op == '<':
            flag = version < nv
        else:
            log.error("Can't support operator %s when check redis version" %
                _op)
        if not flag:
            log.error('Redis version %s is not matched what you want %s' %
                (redis_version, _v))
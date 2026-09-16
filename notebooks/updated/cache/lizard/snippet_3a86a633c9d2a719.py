def clean_old_jobs():
    serv = _get_serv(ret=None)
    ret_jids = serv.keys('ret:*')
    living_jids = set(serv.keys('load:*'))
    to_remove = []
    for ret_key in ret_jids:
        load_key = ret_key.replace('ret:', 'load:', 1)
        if load_key not in living_jids:
            to_remove.append(ret_key)
    if to_remove:
        serv.delete(*to_remove)
        log.debug('clean old jobs: %s', to_remove)
def get_load(jid):
    serv = _get_serv(ret=None)
    sql = "select load from jids where jid = '{0}'".format(jid)
    log.debug('>> Now in get_load %s', jid)
    data = serv.query(sql)
    log.debug('>> Now Data: %s', data)
    if data:
        return data
    return {}
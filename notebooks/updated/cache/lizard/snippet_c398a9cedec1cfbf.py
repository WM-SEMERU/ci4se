def unlock():
    conn = __proxy__['junos.conn']()
    ret = {}
    ret['out'] = True
    try:
        conn.cu.unlock()
        ret['message'] = 'Successfully unlocked the configuration.'
    except jnpr.junos.exception.UnlockError as exception:
        ret['message'
            ] = 'Could not unlock configuration due to : "{0}"'.format(
            exception)
        ret['out'] = False
    return ret
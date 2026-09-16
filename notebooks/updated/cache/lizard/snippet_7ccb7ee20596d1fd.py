def add_store(name, store, saltenv='base'):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    cert_file = __salt__['cp.cache_file'](name, saltenv)
    if cert_file is False:
        ret['result'] = False
        ret['comment'] += 'Certificate file not found.'
    else:
        cert_serial = __salt__['certutil.get_cert_serial'](cert_file)
        serials = __salt__['certutil.get_stored_cert_serials'](store)
        if cert_serial not in serials:
            out = __salt__['certutil.add_store'](name, store)
            if 'successfully' in out:
                ret['changes']['added'] = name
            else:
                ret['result'] = False
                ret['comment'] += 'Failed to store certificate {0}'.format(name
                    )
        else:
            ret['comment'] += '{0} already stored.'.format(name)
    return ret
def remove(name, log_file=None):
    ret = {'name': name, 'changes': {}, 'result': None, 'comment': ''}
    config = __salt__['logadm.list_conf']()
    if not log_file:
        if name.startswith('/'):
            log_file = name
            name = None
        else:
            for log in config:
                if 'entryname' in config[log] and config[log]['entryname'
                    ] == name:
                    log_file = config[log]['log_file']
                    break
    if not name:
        for log in config:
            if 'log_file' in config[log] and config[log]['log_file'
                ] == log_file:
                if 'entryname' in config[log]:
                    name = config[log]['entryname']
                break
    if log_file in config:
        res = __salt__['logadm.remove'](name if name else log_file)
        ret['result'] = 'Error' not in res
        if ret['result']:
            ret['comment'] = 'Configuration for {} removed.'.format(log_file)
            ret['changes'][log_file] = None
        else:
            ret['comment'] = res['Error']
    else:
        ret['result'] = True
        ret['comment'] = 'No configuration for {} present.'.format(log_file)
    return ret
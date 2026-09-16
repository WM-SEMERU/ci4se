def is_present(name, **kwargs):
    ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
    try:
        object_id = __salt__['zabbix.get_object_id_by_params']('template',
            {'filter': {'name': name}}, **kwargs)
    except SaltException:
        object_id = False
    if not object_id:
        ret['result'] = False
        ret['comment'] = 'Zabbix Template "{0}" does not exist.'.format(name)
    else:
        ret['result'] = True
        ret['comment'] = 'Zabbix Template "{0}" exists.'.format(name)
    return ret